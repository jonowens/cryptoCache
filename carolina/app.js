const pinkContractAddress = "";
const blueContractAddress = "";
​
const dApp = {
    ethEnabled: function () {
        if (window.ethereum) {
            window.web3 = new Web3(window.ethereum);
            window.ethereum.enable();
            return true;
        }
        return false;
    },
​
    collectForm: async function () {
        return {
            firstName: $("#dapp-copyright-name").val(),
            lastName: $("#dapp-copyright-lastname").val(),
            streetAddress: $("#dapp-copyright-address").val(),
            city: $("#dapp-copyright-city").val(),
            state: $("#dapp-copyright-state").val(),
            zipCode: Number($("#dapp-copyright-zipcode").val())
        }
    },
​
    buyCoin: async function (coinColor) {
        let formData = this.collectForm();
​
        let contractColor = 
            coinColor === "pink" 
            ? this.pinkContract 
            : this.blueContract;
​
        contractColor.methods.orderPrint(...Object.values(formData))
            .send({from:this.accounts[0]})
            .on("receipt", (receipt)=>{
                console.log(receipt);
                //await fetch("JONATHANS PYTHON SERVER HERE");
                
            })
​
     },
​
    updateUI: async function () { },
​
    main: async function () {
        if (!this.ethEnabled()) {
            alert("Please install MetaMask!");
        }
​
        this.accounts = await window.web3.eth.getAccounts();
        this.pinkContractAddress = pinkContractAddress;
        this.blueContractAddress = blueContractAddress;
​
        this.pinkJson = await (await fetch("./pinkContract.json")).json();
​
        this.pinkContract = new window.web3.eth.Contract(
            this.pinkJson,
            this.pinkContractAddress,
            { defaultAccount: this.accounts[0] }
        );
​
​
        this.blueJson = await (await fetch("./blueContract.json")).json();
​
        this.blueContract = new window.web3.eth.Contract(
            this.blueJson,
            this.blueContractAddress,
            { defaultAccount: this.accounts[0] }
        );
​
​
        await this.updateUI();
​
    }
}
​
dApp.main();
