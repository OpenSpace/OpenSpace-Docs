(function () {
    'use strict';

    class Topic {
        /**
         * Construct a topic. (Only for internal use)
         *
         * @param iterator - An async iterator to represent data from OpenSpace
         * @param talk - The function used to send messages
         * @param cancel - The function used to cancel the topic
         */
        constructor(iterator, talk, cancel) {
            this._iterator = iterator;
            this._talk = talk;
            this._cancel = cancel;
        }
        /**
         * Send a message to OpenSpace through the topic. The shape of the message should match
         * the topic payload type. See @TODO (anden 2026-04-14): url to documentation page for
         * the available topic types and their payload shapes.
         *
         * @param data The Javascript object to send. Must be possible to encode into JSON
         */
        talk(data) {
            this._talk(data);
        }
        /**
         * Allow for-await loops on the topic object. The topic will yield data from OpenSpace
         * until it is cancelled or the connection is lost.
         * Example usage:
         * `for await (const data of topic) { ... }`
         */
        [Symbol.asyncIterator]() {
            return this._iterator;
        }
        /**
         * Get the next data package from OpenSpace. This will wait until the next data package
         * is received. This function can be used in combination with `startTopic` to get data
         * from OpenSpace. Note that you can also use for-await-of loops to iterate through the
         * topic data, which might be more convenient depending on your use case.
         *
         * @returns The next awaited data package from OpenSpace
         */
        async next() {
            const result = await this._iterator.next();
            if (result.done) {
                throw new Error('Topic iterator completed unexpectedly.');
            }
            return result.value;
        }
        /**
         * Cancel the topic subscription. After calling this function, the topic will no longer
         * yield data from OpenSpace, and any resources associated with the topic on the
         * OpenSpace server will be freed. Note that after cancelling, the topic object should
         * not be used anymore.
         */
        cancel() {
            return this._cancel();
        }
        _iterator;
        _talk;
        _cancel;
    }

    const ApiVersion = {
        type: 'apiHandshake',
        apiVersion: {
            major: 1,
            minor: 0,
            patch: 0
        }
    };
    class OpenSpaceApi {
        _callbacks = {};
        _nextTopicId = 0;
        _socket;
        _userOnConnect = null;
        /**
         * Construct an instance of the OpenSpace API.
         *
         * @param socket - An instance of Socket or WebSocket. The socket should not be
         * connected prior to calling this constructor.
         */
        constructor(socket) {
            socket.onMessage((message) => {
                try {
                    const messageObject = JSON.parse(message);
                    if (messageObject.topic !== undefined) {
                        const callback = this._callbacks[messageObject.topic];
                        if (callback && 'payload' in messageObject) {
                            callback(messageObject.payload);
                        }
                    }
                }
                catch (e) {
                    console.error(`Error handling message from OpenSpace: ${e}\nMessage: ${message}`);
                }
            });
            this._socket = socket;
            this._socket.onConnect(() => {
                // Always send API handshake before any user-registered onConnect
                this._sendHandshake();
                // Call user defined onConnect if it exists
                this._userOnConnect?.();
            });
        }
        _sendHandshake() {
            this._socket.send(JSON.stringify(ApiVersion));
        }
        /**
         * Set connect callback.
         *
         * @param callback - The function to execute when connection is established.
         */
        onConnect(callback) {
            this._userOnConnect = callback;
        }
        /**
         * Set disconnect callback.
         *
         * @param callback - The function to execute when socket is disconnected.
         */
        onDisconnect(callback) {
            this._socket.onDisconnect(callback);
        }
        /**
         * Connect to OpenSpace.
         */
        connect() {
            this._socket.connect();
        }
        /**
         * Disconnect from OpenSpace.
         */
        disconnect() {
            this._socket.disconnect();
        }
        /**
         * Initialize a new channel of communication
         *
         * @param type - A string specifying the type of topic to construct. See OpenSpace's
         * server module for available topic types.
         * @param payload - An object containing the data to send to OpenSpace when initializing
         * the topic.
         * @param cancelPayload - An optional object containing the data to send to OpenSpace
         * as a last message before cancelling and closing the topic.
         * @return An object representing the topic.
         */
        startTopic(type, payload, cancelPayload) {
            const topicID = this._nextTopicId++;
            const messageObject = {
                topic: topicID,
                type,
                payload
            };
            this._socket.send(JSON.stringify(messageObject));
            // `cancelPromise` resolves when the topic is cancelled, which causes the iterator to
            // stop yielding and the callback to be cleaned up. @TODO (anden88: 2025-05-05): does
            // the topic cancel correctly if we're still waiting for data that hasn't received yet?
            let resolveCancel = () => { };
            const cancelPromise = new Promise((resolve) => (resolveCancel = resolve));
            const promise = () => {
                return new Promise((resolve) => {
                    // The callback stores all active topics each with a different payload data type
                    // so we can't get away from casting the payload as unknown here.
                    this._callbacks[topicID] = resolve;
                    cancelPromise.then(() => {
                        delete this._callbacks[topicID];
                    });
                });
            };
            const iterator = (async function* () {
                try {
                    while (true) {
                        yield await promise();
                    }
                }
                catch (e) {
                    return;
                }
            })();
            const talk = (payload) => {
                const messageObject = {
                    topic: topicID,
                    payload
                };
                this._socket.send(JSON.stringify(messageObject));
            };
            const cancel = () => {
                if (cancelPayload !== undefined) {
                    talk(cancelPayload);
                }
                resolveCancel();
            };
            return new Topic(iterator, talk, cancel);
        }
        /**
         * Authenticate this client. This must be done if the client is not whitelisted in
         * openspace.cfg.
         *
         * @param secret - The secret used to authenticate with OpenSpace.
         */
        async authenticate(secret) {
            const topic = this.startTopic('authorize', { password: secret });
            try {
                return await topic.next();
            }
            catch (e) {
                throw new Error(`Authentication error: ${e}\n`);
            }
            finally {
                topic.cancel();
            }
        }
        /**
         * Set the property value.
         *
         * @param property - The URI of the property to set.
         * @param value - The value to set the property to.
         */
        setProperty(property, value) {
            const topic = this.startTopic('set', { property, value });
            topic.cancel();
        }
        async getProperty(property, expectedType) {
            const topic = this.startTopic('get', { property });
            try {
                const data = await topic.next();
                if (expectedType === undefined) {
                    return data;
                }
                if (data.type === 'property') {
                    const propertyType = data.value.metaData.type;
                    if (propertyType !== expectedType) {
                        throw new Error(`Expected: '${expectedType}' but property '${property}' is of type '${propertyType}'`);
                    }
                }
                return data;
            }
            catch (e) {
                throw new Error(`Error getting property. ${e}\n`);
            }
            finally {
                topic.cancel();
            }
        }
        async getDocumentation(type) {
            const topic = this.startTopic('documentation', { type });
            try {
                return await topic.next();
            }
            catch (e) {
                throw new Error(`Error getting documentation: ${e}\n`);
            }
            finally {
                topic.cancel();
            }
        }
        subscribeToProperty(property, expectedType) {
            const topic = this.startTopic('subscribe', { event: 'start_subscription', uri: property }, { event: 'stop_subscription' });
            if (expectedType === undefined) {
                return topic;
            }
            const expected = expectedType;
            async function* narrowedIterator() {
                // MetaData object is the first value to be returned by OpenSpace
                for await (const data of topic) {
                    if (data.type === 'metaData') {
                        if (data.metaData.type !== expected) {
                            topic.cancel();
                            throw new Error(`Expected: '${expected}' but property '${property}' is of type: '${data.metaData.type}'`);
                        }
                        yield data;
                    }
                    else if (data.type === 'value') {
                        yield data;
                    }
                    else {
                        throw new Error(`Missing case for data package: '${data}'`);
                    }
                }
            }
            return {
                next: async () => {
                    const result = await narrowedIterator().next();
                    if (result.done) {
                        throw new Error('Topic iterator completed unexpectedly.');
                    }
                    return result.value;
                },
                [Symbol.asyncIterator]: narrowedIterator,
                talk: (data) => topic.talk(data),
                cancel: () => topic.cancel()
            };
        }
        // @TODO (anden88: 2026-05-06): Right now any lua function will create a new topic.
        // should we instead let the class keep one reference to the luascript topic and this
        // function uses the topic.talk to pass the new scripts, returning data as necessary
        // only arguably benefit would be that we don't create a bunch of topics that gets
        // immediately destroyed
        /**
         * Execute a Lua script.
         *
         * @param script - The Lua script to execute.
         * @param getReturnValue - Specified whether the return value should be collected.
         * @param shouldBeSynchronized - Specified whether the script should be synchronized on
         * a cluster.
         * @return The return value of the script, if `getReturnValue` is true, otherwise
         * undefined.
         */
        async executeLuaScript(script, getReturnValue = true, shouldBeSynchronized = true) {
            const topic = this.startTopic('luascript', {
                script,
                return: getReturnValue,
                shouldBeSynchronized
            });
            if (!getReturnValue) {
                topic.cancel();
                return;
            }
            try {
                const response = await topic.next();
                return response;
            }
            catch (e) {
                throw new Error(`Error executing lua script: ${e}\n`);
            }
            finally {
                topic.cancel();
            }
        }
        async executeLuaFunction(fun, args, getReturnValue = true) {
            const topic = this.startTopic('luascript', {
                function: fun,
                arguments: args,
                return: getReturnValue
            });
            if (!getReturnValue) {
                topic.cancel();
                return;
            }
            try {
                const response = await topic.next();
                return response;
            }
            catch (e) {
                throw new Error(`Error executing lua function: ${e}\n`);
            }
            finally {
                topic.cancel();
            }
        }
        /**
         * Get an object representing the OpenSpace Lua library.
         *
         * @return The Lua library, mapped to async JavaScript functions.
         */
        async library() {
            const generateAsyncFunction = (functionName) => {
                return async (...args) => {
                    try {
                        const luaTable = await this.executeLuaFunction(functionName, args);
                        if (luaTable) {
                            return luaTable[1];
                        }
                        return null;
                    }
                    catch (e) {
                        throw new Error(`Lua execution error: ${e}\n`);
                    }
                };
            };
            let documentation;
            try {
                documentation = await this.getDocumentation('lua');
            }
            catch (e) {
                throw new Error(`Failed to get documentation: ${e}\n`);
            }
            const jsLibrary = {};
            documentation.forEach((library) => {
                if (library.name === '') {
                    // Direct openspace.* function add to top level
                    library.functions.forEach((f) => {
                        const fullFunctionName = `openspace.${f.name}`;
                        jsLibrary[f.name] = generateAsyncFunction(fullFunctionName);
                    });
                }
                else {
                    // Namespaced function, create sub-library
                    const subLibrary = {};
                    library.functions.forEach((f) => {
                        const fullFunctionName = `openspace.${library.name}.${f.name}`;
                        subLibrary[f.name] = generateAsyncFunction(fullFunctionName);
                    });
                    jsLibrary[library.name] = subLibrary;
                }
            });
            return jsLibrary;
        }
    }

    class WebSocketWrapper {
        constructor(address, port) {
            this._address = address;
            this._port = port;
            this._onConnect = () => { };
            this._onDisconnect = () => { };
            this._onMessage = () => { };
        }
        onConnect(callback) {
            this._onConnect = callback;
        }
        onDisconnect(callback) {
            this._onDisconnect = callback;
        }
        onMessage(callback) {
            this._onMessage = (event) => {
                callback(event.data);
            };
        }
        connect() {
            this._client = new WebSocket(`ws://${this._address}:${this._port}`);
            this._client.onopen = this._onConnect;
            this._client.onclose = () => {
                this._onDisconnect();
                this._client = null;
            };
            this._client.onmessage = this._onMessage;
        }
        send(message) {
            if (!this._client) {
                throw new Error('Cannot send: socket is not connected');
            }
            this._client.send(message);
        }
        disconnect() {
            if (!this._client) {
                return;
            }
            this._client.close();
            this._client = null;
        }
        _address;
        _port;
        _client = null;
        _onConnect;
        _onDisconnect;
        _onMessage;
    }

    window.openspaceApi = (address = 'localhost', port = 4682) => new OpenSpaceApi(new WebSocketWrapper(address, port));

})();
