pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract FujiCollectable is ERC721, VRFConsumerBase {

    bytes32 internal keyHash;
    uint256 public fee;

    mapping(bytes32 => address) public requestIdToSender;
    mapping(bytes32 => string) public requestIdToTokenURI;
    event requestedCollectible(bytes32 indexed requestId);

    constructor(address _VRFCoordinator, address _LinkToken, bytes32 _keyhash) public
    VRFConsumer(_VRFCoordinator, _LinkToken)
    ERC721("FujiPhotographs", "FUJI")
    {
        keyHash = _keyhash;
        fee = 0.1 * 10 ** 18; // 0.1 LINK 1000000000000000000
    }

    function createCollectible(uint256 userProvidedSeed, string memory tokenURI)
    public returns (bytes32){
        bytes32 requestId = requestRandomness(keyHash, fee, userProvidedSeed);
        requestIdToSender[requestId] = msg.sender;
        requestIdToTokenURI[requestId] = tokenURI;
        emit requestedCollectible(requestId);
    }
}