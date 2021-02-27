# CryptoCache:

We are to develop a 3D printing e-commerce using blockchain (ethereum).

<img src="Images/867.gif" width=150 height=150 align="left"/> The e-commerce sells a selection of `3D templates ethereum coins`, which can be ordered in either blue or pink. Depending on the selection, the buyer `pays` in ether and send the order to the 3D printer `third party` provider. 

The project is anticipated to consists of  3 sections, with each section developed with its own blockchain address. The three sections are:

&ensp; **Front End:** Interacts with the customer purchases and consists of one file with 1 contract. This contract receives money from an address (buyer address) and sends ether to a third party address. 

&ensp; **Back End:** This section is expected to consist of two contracts: one that interacts with the `Front end module` and the second contract that interacts with the 3D printing provider. This section will have access to the stensil files (stored in Pinata), send the extracted file to 3d printer provider, and pays the provider for the services (in Ether).

&ensp; **web application** hosts the e-commerce for viewing and selection. The webhosting is also using blockchain, so that the display is permanent. 

See below for project configuration.

![proposal modules](Images/proposal_modules.png)

## Resources:

[1] https://developers.shapeways.com/quick-start




