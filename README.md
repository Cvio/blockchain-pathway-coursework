# blockchain-pathway-coursework
For submitting assignments for the Blockchain Pathway
# Module 4 Challenge
### Step 1: Create the KaseiCoin Token Contract (10 points)
Code the KaseiCoin contract. (5 points)
Take a screenshot of the successful compilation of the contract, and add it to the Evaluation Evidence section of the README.md file for your Challenge repository. (5 points)

*Completed*

### Step 2: Create the KaseiCoin Crowdsale Contract (15 points)
Have your KaseiCoinCrowdsale contract inherit the OpenZeppelin Crowdsale and MintedCrowdsale contracts. (5 points)
Add the rate, wallet, and token parameters to your crowdsale contract’s constructor. (5 points)
Take a screenshot of the successful compilation of the contract, and add it to the Evaluation Evidence section of the README.md file for your Challenge repository. (5 points)

*Completed*
### Step 3: Create the KaseiCoin Deployer Contract (35 points)
Add variables to the KaseiCoinCrowdsaleDeployer contract that can store the KaseiCoin and KaseiCoinCrowdsale contract addresses. (5 points)
Add the name, symbol, and wallet parameters to the KaseiCoinCrowdsaleDeployer contract’s constructor. (10 points)
Add the required code within the constructor’s body. (15 points)
Take a screenshot of the successful compilation of the contract, and add it to the Evaluation Evidence section of the README.md file for your Challenge repository. (5 points)

*Completed*
### Step 4: Deploy the Crowdsale to a Local Blockchain (30 points)
Record a short video or take screenshots as evidence of your deployed crowdsale contract. The video or screenshots should illustrate the following: (30 points)
Deployment of the contract to a local blockchain with Remix, MetaMask, and Ganache.
Using test accounts to buy new tokens from the crowdsale and then checking the balances associated with the test accounts.
After purchasing tokens with test accounts, viewing the total supply of minted tokens and the amount of wei that has been raised by the crowdsale.

*Completed*

IMPORTANT
If you provide screenshots, add them to the README.md file of your Challenge repository. The screenshots should provide a guide that someone else could use to compile the contracts and add the KaseiCoin token to MetaMask.

Coding Conventions and Formatting (10 points)

*Completed*

To receive all points, you must:
Place imports at the top of the file. (3 points)
Name functions and variables using mixedCase, as stated in the Solidity Language Style Guide (Links to an external site.). (2 points)
Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. (3 points)
Use concise logic and creative engineering where possible. (2 points)

*Completed*

# Evaluation Evidence
In order for your submission to be graded, you must create a section in the README.md file of your GitHub repository called Evaluation Evidence, where you will share screenshots of your work.
## Compile Contracts

### 01
[KaseiCoin Contract Compiled](/Evaluation_Evidence/01-kasei_coin_compiled.png)
### 02
[KaseiCoinCrowdsale Contract Compiled](/Evaluation_Evidence/02-kasei_coin_crowdsale_compiled.png)
### 03
[KaseiCoinCrowdsale Contract Compiled](/Evaluation_Evidence/03-kasei_coin_crowdsale_deployer_compiled.png)

## Add Network to Metamask from Ganache
### 01
[Open Metamask and in the Network Pulldown Click Add Network](/Evaluation_Evidence/04-1-add_network_ganache_metamask.png)
### 02
[Open Ganache and Use the URL as the New RPC](/Evaluation_Evidence/04-2-add_network_ganache_metamask.png)
### 03
[Use Chain ID of "1337" and Currency Symbol "ETH"](/Evaluation_Evidence/04-3-add_network_ganache_metamask.png)
### 04
[Test By Changing Remix Env to Injected Provider - Metamask](/Evaluation_Evidence/04-4-add_network_ganache_metamask.png)

## Deploy Contract
### 01
[Deploy](/Evaluation_Evidence/05-1-kasei_coin_contract_deployed.png)
### 02
[Local Blockchain Transaction](/Evaluation_Evidence/06-1-buying_kasei_coin_with_eth.png)
### 03
[Able To Buy and Send](/Evaluation_Evidence/06-2-sending_kasei_from_account.png)
### 04
[Account 1 Balance](/Evaluation_Evidence/06-3-balance_of_account1.png)
### 05
[Account 2 Balance](/Evaluation_Evidence/06-4-balance_of_account1.png)


# ***************************************************************************************


# Module 3 Challenge
 Requirements
 ### Step 1: Create a Joint Savings Account Contract in Solidity (55 points)
Create a new Solidity file named joint_savings.sol. (5 points)
Define a new contract named JointSavings in the Solidity file. (5 points)
Define all the required variables in the contract. (10 points)
Define a withdraw function. (10 points)
Define a deposit function. (10 points)
Define the setAccounts function. (10 points)
Define the fallback function. (5 points)

*Completed*

### Step 2: Compile and Deploy Your Contract in the JavaScript VM (15 points)
Compile your smart contract without errors. (10 points)
Deploy your smart contract in the JavaScript VM. (5 pints)

## *There was no option for JavaScript VM. I looked online and I couldn't find a reference to it. I used Remix VM since it was default.*
[No JavaScript VM](/Execution_Results/00-JavascriptVM_is_not_an_option.png)

*Otherwise completed*

### Step 3: Interact with Your Deployed Smart Contract (30 points)
Use the setAccounts function as requested. Capture a screenshot of the execution, and share it in your final submission. (10 points)
Test the deposit function. After each of the three transactions, capture a screenshot of the execution, and share it in your final submission. (10 points)
Test the withdrawal functionality of the smart contract. Capture a screenshot of the two executions, and share them in your final submission. Additionally, capture screenshots of the terminal output from the lastToWithdraw and lastWithdrawAmount functions. (10 points)

*Completed*

## Screenshots
[Set Accounts](/Execution_Results/01-set_account_addresses.png)
#
[Deposit 1](/Execution_Results/02-deposit_1_ether_as_wei.png)
#
[Deposit 10](/Execution_Results/03-deposit_10_eth_as_wei.png)
#
[Deposit 5](/Execution_Results/04-deposit_5_eth_as_wei.png)
#
[Withdraw 5](/Execution_Results/05-withdraw_5_eth_to_acct_1.png)
#
[Withdraw 10](/Execution_Results/06-withdraw_10_eth_to_acct_2.png)
#
[Console Img](/Execution_Results/09-lastToWithdraw_and_lastWithdrawAmount.png)
#
[Full Deploy](/Execution_Results/07-full-deploy_pic.png)

# ***************************************************************************************

# Module 2 Challenge
 Requirements
### Import Ethereum Transaction Functions into the Fintech Finder Application (30 points)
Import generate_account, get_balance, and send_transaction from the crypto_wallet.py file. (10 points)
Call the generate_account function and store the account object. (10 points)
Call the get_balance function and pass it the Ethereum account.address. (10 points)

*Completed*

### Sign and Execute a Payment Transaction (20 points)
Calculate the transaction’s total wage. (10 points)
Call the send_transaction function and pass it the account, candidate_address, and wage parameters. (5 points)
Return the transaction hash from the send_transaction and display it on the application’s web interface. (5 points)

*Completed*

### Inspect the Transaction on Ganache (20 points)
Send a transaction using the Fintech Finder app, and then use the returned transaction hash to verify the transaction oin Ganache. On the top left corner of the Ganache application there is a button labeled "Accounts", next to it there is one labeled "Blocks", then one labeled "Transactions". Click the "Transactions" button to view the recent transactions. (10 points)
In your README.md file, provide screenshots from Ganache that show the sender’s address balance and history, and the recipient's address balance and history. (10 points)

*Completed*

### Coding Conventions and Formatting (10 points)
Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. (3 points)
Name functions and variables with lowercase characters, with words separated by underscores. (2 points)
Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. (3 points)
Use concise logic and creative engineering where possible. (2 points)

*Completed*

### Deployment and Submission (10 points)
Submit a link to a GitHub repository that’s cloned to your local machine and that contains your files. (4 points)
Use the command line to add your files to the repository. (3 points)
Include appropriate commit messages for your files. (3 points)

*Completed*

### Comments (10 points)
Be well commented with concise, relevant notes that other developers can understand. (10 points)

*Completed*

# Before
[before](trans_before.png)

# Success!
[validated](trans_validated.png)

# After
[after](trans_after.png)

# Transactions
[record](trans_record.png)

# Log Pic
[log](trans_log.png)

# ***************************************************************************************

# Module 1 Challenge
 Requirements
### Step 1: Create a Record Data Class (20 points)
Successfully define a new class named Record. (10 points)
Implement the required class attributes for the Record class. (10 points)

*Completed*

### Step 2: Modify the Existing Block Data Class to Store Record Data (20 points)
Rename the data attribute in the Block class to record. (10 points)
Set the data type of the record attribute to Record. (10 points)

*Completed*

### Step 3: Add Relevant User Inputs to the Streamlit Interface (20 points)
Add the correct user inputs for getting the sender, receiver, and amount. (10 points)
Correctly update the Add Block button functionality. (10 points)

*Completed*

### Step 4: Test the PyChain Ledger by Storing Records (10 points)
Test the functionality of your chain. In the README.md file for your GitHub repository, include a screenshot that contains a blockchain consisting of several blocks. (5 points)
Confirm that your blockchain is valid. In the README.md file of your GitHub repository, include a screenshot of the Streamlit application page displaying “Blockchain is Valid.” (5 points)

*Completed*

### Coding Conventions and Formatting (10 points)
Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. (3 points)
Name functions and variables with lowercase characters, with words separated by underscores. (2 points)
Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. (3 points)
Use concise logic and creative engineering where possible. (2 points)

*Completed*

### Deployment and Submission (10 points)
Submit a link to a GitHub repository that’s cloned to your local machine and that contains your files. (4 points)
Use the command line to add your files to the repository. (3 points)
Include appropriate commit messages for your files. (3 points)

*Completed*

### Comments (10 points)
Be well commented with concise, relevant notes that other developers can understand. (10 points)

*Completed*

# Success!
[screenshot](screenshot.png)