// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract fundMe {
    mapping(address => uint256) public addressToAmountFunded;
    address public owner;
    address[] public funders;
    AggregatorV3Interface public priceFeed;


    constructor(address _priceFeedAddress) public{
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner, 'You are not the owner !');
        _;
    }

    function fund() public payable {
        // uint256 minimumUSD = 50*(10**18);
        uint256 minimumUSD = 50;

        require(getConversionRate(msg.value)>=minimumUSD, 'You need to spend more ETH!');
        addressToAmountFunded[msg.sender] = msg.value;
        funders.push(msg.sender);
    }

    function getPrice() public view returns(uint256){
        // AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
         return uint256(answer * 10000000000);
    }

    function getConversionRate(uint256 ethAmmount) public view returns(uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmmountInUSD = (ethPrice*ethAmmount)/1000000000000000000;
        return ethAmmountInUSD;

    }

    function withdraw() public onlyOwner payable{
        
        msg.sender.transfer(address(this).balance);
    }

    
    function contractBalance() public view returns(uint256){
        return address(this).balance;
    }
}