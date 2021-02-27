pragma solidity ^0.5.0;

// First contract page 27
contract Faucet {
    
    // Give out Ether to anyone who asks
    function withdraw(uint withdraw_amount) public {
        
        // Limit withdrawal amount 
        require(withdraw_amount <= 100000000000000000);
        
        // Send the amount to the address that requested it 
        msg.sender.transfer(withdraw_amount);
        
    }
    
    // Function to accept money into the contract (fallback function)
    function () external payable {}
}