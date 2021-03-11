pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";

contract PinkCoin is ERC721Full {
    

    constructor() ERC721Full("PinkToken", "PINKT") public {
        
        
    }
    
    
    using Counters for Counters.Counter;
        Counters.Counter tokenIds;

    struct OrderData {
        
        address buyer;
        string country;
        string state;
        string city;
        string streetAddress;
        uint zipCode;

    }

    mapping(uint => OrderData) public colorToken;

    event tokenOrder(uint tokenId);
    
    
    function orderPrint(
        
        address buyer, 
        string memory country,
        string memory state,
        string memory city,
        string memory streetAddress,
        uint zipCode
        
        ) public payable returns(uint) {
        
       
        uint price = 10000000000000;
        uint pricePaid = msg.value;
        require (pricePaid >= price, "You need to deposit exactly 10000000000000 wei!");
        
        
        tokenIds.increment();
        uint tokenId = tokenIds.current();

        _mint(buyer, tokenId);
      
        colorToken[tokenId] = OrderData(
            
            buyer,
            country,
            state,
            city,
            streetAddress,
            zipCode
            
            );

        emit tokenOrder(tokenId);
        
        return tokenId;
        
    }
    
    
    function withdraw(uint amount, address payable recipient) public {
        
    require(recipient == 0xA31b61b2aea2d93a3d424523a612e518F5aCA407 || recipient == 0x9C6a00F697354e0178a4e2C805718Ce10276839C, "You don't own this contract!");
      
      recipient.transfer(amount);

    }
    
    // Function to accept money into the contract (fallback function)
    
    function () external payable {}

}