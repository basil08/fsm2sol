# fsm2sol - smart contracts as FSMs! 

Rethink your contract logic as a FSM. Modelling contracts as FSMs help identify logical bugs during development and provides a formally sound assurance of the correctness of the contract logic. 

## Why to write contract as FSMs? 

Market cap of ETH and BTC 

For example: TheDAO attack 

Migration of core financial applications into web3 space. 

Auditing contracts not enough! We need mathematical guarantee! 

Field of Formal Verification 

Why not start thinking of contracts as FSMs before writing a single line of code? 

Enter `fsm2sol`

![](/assets/img/2.png)

## Formal definition of the FSM

![](/assets/img/0.png)

## Transformation specification

### FSM inputs 

![](/assets/img/1.png)

## Roadmap

1. Define grammar for input YAML
2. Check if input FSM specification is well-formed. If not, give corrective error messages.
3. Implement a graphical interface which generates the input YAML. This allows users to never touch text editor and start deploying smart contracts. 
4. Run the generated .sol through a formatter

## Reference 

1. [Designing Secure Ethereum Smart Contracts: A FSM based approach][0].

## Future work (Theoretical)

Prove the equivalence of Solidity language and set of FSMs - is the FSM specification expressive enough to represent all possible Solidity contracts?

## Scope for improvements (Technical)

1. Extend the transformer to express modifiers/other access specifiers (Section 5 of the paper: `Plugins`)
2. Make the GUI implement a "one button tap deploy" paradigm for onboarding next gen of web3 developers and accelerate development for experienced developers.

## Contributing 

Open to PRs!

## License 

MIT 

[0]: https://arxiv.org/pdf/1711.09327.pdf
