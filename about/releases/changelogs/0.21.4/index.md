This patch mainly fixes an issue with the Celestrak data retrieval. One error is an invalid SSL certificate that prevented successful downloads and the other is in planetarium environments where multiple computers were unable to retrieve datasets for active satellites and Starlink. The patch fixes both issues by using a new OpenSpace relay server that caches the data.

# Bug Fixes
  - Update satellite trails to use new relay server
  - Prevent crash when a session recording includes a malformed setPropertyValue command
  - Fix issues with the New York map layers not loading correctly (#3890)
  - Fix crash that would occur when an asset includes itself
