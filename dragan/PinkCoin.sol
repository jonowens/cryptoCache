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
        
       
        uint price = 1000000000000000000;
        uint pricePaid = msg.value;
        require (pricePaid >= price);
        
        
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
    
}