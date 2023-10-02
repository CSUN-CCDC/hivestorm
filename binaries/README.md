These are binaries to use in the hivestorm competition, either statically compiled, or generated with tools like nix-bundle. 


After trying many, many tools to create portable binaries, I gave up and eventually settled on [nix-portable](https://github.com/DavHau/nix-portable/). It just worked, and it is very easy to clean up. 

To install nix-portable:

`curl https://github.com/DavHau/nix-portable/releases/download/v009/nix-portable -o /bin/nix-portable`

Or use wget, since sometimes curl isn't installed by default.

`chmod +x /bin/nix-portable`

Then cd into this git repo, 