# Skybrowser Webpage Design
In this document I will explain how the sky browser webpage is structured and explain some design choices.

## Architecture overview
When looking at the `sky_browser` repository, you can see that there are two folders - `public_openspace` and `public_gui`. These are the two webpages that are loaded by OpenSpace and the WebUI, respectively, when using the sky browser. In OpenSpace the webpage is loaded as a webpage in a CEF browser, and in the UI it is loaded in an iframe.

The `public_openspace` code ande the `public_gui` code are pretty similar, except for the `functions.js` file. The GUI webpage contains functions to handle messages from the UI to communicate its state, and the OpenSpace code contains functionality to connect to the OpenSpace api. It was necessary to split this webpage into two to ensure that the UI webpage doesn't connect to the OpenSpace API.

Both the `public_openspace` and the `public_gui` webpage features an iframe where the WorldWideTelescope app is loaded.

## Messages to and from WorldWideTelescope
Since we need to communicate with the WWT app, we use the standard web Window API to post messages (https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage). This is done by posting messages to the iframe. In order to do that, we need to meet certain security standards. It is not possible to post messages to just about any iframe since that is a security hole. Therefore, you need to specify what website the iframe allows messages from. This is done with the url variable `origin`. A variable can be inserted into the url for use with php with the prefix `?`. If we insert `?origin="url"`, we can specify the origin of the iframe, i.e. the webpage we will allow messages to come from. For example, in the `public_openspace` folder we find this code:

index.html
```html
<iframe
	id="wwtResearch"
	name="wwt"
	src="http://wwtapp.openspaceproject.com/1/?origin=http://wwt.openspaceproject.com"
	allow="accelerometer; clipboard-write; gyroscope"
	allowfullscreen
	frameborder="0"
	align="middle"
>
```

functions.js
```js
function sendMessageToWWT(message) {
  try {
    var frame = document.getElementsByTagName("iframe")[0].contentWindow;
    frame.postMessage(message, "http://wwtapp.openspaceproject.com/");
  } catch (error) {}
}
```

The important parts of the code are these:

index.html
```js
src="http://wwtapp.openspaceproject.com/1/?origin=http://wwt.openspaceproject.com"
```

functions.js
```js
frame.postMessage(message, "http://wwtapp.openspaceproject.com/");
```

The WorldWideTelescope application is hosted on the url http://wwtapp.openspaceproject.com/1/. The messages that we post in the `functions.js` is set to have their `targetOrigin` set to the url that the iframe loads: http://wwtapp.openspaceproject.com. To accept the message, the iframe needs to specify its origin to the same url that is posting the messages. In this case, the `public_gui` and `public_openspace` webpages are hosted on the url `http://wwt.openspaceproject.com`. Because of the `?origin=http://wwt.openspaceproject.com` parameter sent to the WWT application, WWT can accept the incoming messages from that domain.

***Note: only the domain needs to be specified - it doesn't have to be the exact same url***
