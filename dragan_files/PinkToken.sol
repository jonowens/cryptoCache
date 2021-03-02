pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";

contract Memorabillia is ERC721Full {

    constructor() ERC721Full("PinkToken", "PNKT") public {
        
    }
    
    uint price = 1000000000000000000;
    
    
    using Counters for Counters.Counter;
        Counters.Counter token_ids;

    struct ColorToken {
        string name;
        string description;
        uint price;

    }

    mapping(uint => ColorToken) public memorabillia_collection;

    event tokenOrder(uint token_id, uint price, string order_uri);

    function orderPrint(address buyer, string memory name, string memory description, uint price_paid, string memory token_uri) public payable returns(uint) {
        token_ids.increment();
        uint token_id = token_ids.current();

        _mint(buyer, token_id);
        _setTokenURI(token_id, token_uri);
      
        memorabillia_collection[token_id] = ColorToken(name, description, price_paid);

        return token_id;
        
    }
}