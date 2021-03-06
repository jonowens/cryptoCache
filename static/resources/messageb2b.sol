pragma solidity ^0.5.0;

contract messageb2b {
    
    string myURL;
    uint orderN;
    
    function SetmyURLinfo(string memory _myURL) public {
        myURL = _myURL;
    }
    
    function GetmyURLinfo() public view returns (string memory){
        return (myURL);
    }
}