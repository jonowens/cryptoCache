pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";

contract Memorabilia is ERC721Full {

    constructor() ERC721Full("PinkToken", "PNKT") public {
        
    }
    
    
    using Counters for Counters.Counter;
        Counters.Counter token_ids;

    struct OrderData {
        
        string firstName;
        string lastName;
        string country;
        string state;
        string city;
        string street_address;
        uint zipCode;

    }

    mapping(uint => OrderData) public memorabilia_token;

    event tokenOrder(uint token_id, uint price, string order_uri);
    
    
    function orderPrint(
        
        address buyer, 
        string memory firstName,
        string memory lastName,
        string memory country,
        string memory state,
        string memory city,
        string memory street_address,
        uint zipCode,
        string memory token_uri
        
        ) public payable returns(uint) {
        
       
        uint price = 1000000000000000000;
        uint price_paid = msg.value;
        require (price_paid >= price);
        
        
        token_ids.increment();
        uint token_id = token_ids.current();

        _mint(buyer, token_id);
        _setTokenURI(token_id, token_uri);
      
        memorabilia_token[token_id] = OrderData(
            
            firstName,
            lastName,
            country,
            state,
            city,
            street_address,
            zipCode
            
            );

        return token_id;

    }
    
}