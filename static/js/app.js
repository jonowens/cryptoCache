// let provider = ethers.getDefaultProvider('kovan');
let web3 = new Web3(Web3.givenProvider || "ws://localhost:8545");
// let provider = new ethers.providers.Web3Provider(web3.currentProvider);

const pinkContractAddress = "0x3607844eb2eC711279B2F1831E1784Bc7423713f";
const blueContractAddress = "0xC86C8d3E16370dd76e73DdeEf15767E343331816";

const dApp = {
    ethEnabled: function () {
        if (window.ethereum) {
            window.web3 = new Web3(window.ethereum);
            console.log(web3); //to print out on the console
            window.ethereum.enable();
            return true;
        }
        return false;
    },

    collectForm: async function () {
        return {
            address: $("#dapp-copyright-buyerAddress").val(),
            country: $("#dapp-copyright-country").val(),
            state: $("#dapp-copyright-state").val(),
            city: $("#dapp-copyright-city").val(),
            streetAddress: $("#dapp-copyright-address").val(),
            zipCode: Number($("#dapp-copyright-zipcode").val())
        }
    },

    buyCoin: async function (coinColor) {
        let formData = await this.collectForm();
        
        let contractColor = 
            coinColor === "pink" 
            ? this.pinkContract 
            : this.blueContract;
        // console.log(contractColor.options);
        console.log(Object.values(formData))
        contractColor.methods.orderPrint(...Object.values(formData))
            .send({
                from: this.accounts[0],
                value: 1000000000000000000
            })
            .on("receipt", (receipt)=>{
                
                console.log(receipt);
                
                alert(`Success: ${receipt.transactionHash}`)

                console.log(receipt.transactionHash)
            })
            .catch((err)=> console.log(err))

     },

    updateUI: async function (result) { },

    main: async function () {
        if (!this.ethEnabled()) {
            alert("Please install MetaMask!");
        }

        this.accounts = await window.ethereum.request({ method: 'eth_accounts' });
        
        this.pinkContractAddress = pinkContractAddress;
        this.blueContractAddress = blueContractAddress;

        

        this.pinkJson = await (await fetch("pinkContract")).json();
       
        
        this.pinkContract = new window.web3.eth.Contract(
            this.pinkJson,
            this.pinkContractAddress,
            { defaultAccount: this.accounts[0] }
        );


        this.blueJson = await (await fetch("blueContract")).json();
       
        
        this.blueContract = new window.web3.eth.Contract(
            this.blueJson,
            this.blueContractAddress,
            { defaultAccount: this.accounts[0] }
        );


        await this.updateUI();

    }
}

dApp.main();
