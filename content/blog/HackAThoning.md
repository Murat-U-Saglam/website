---
title: "HackAThoning"
date: 2024-03-27T20:32:02Z
tags: ["Hackathon", "Personal"]
draft: false
---
# Hackathons

Coming from a cyber security background I always found the name hackathons strange, cyber folks are have our group all nighters and we call them CTFs (Capture the flags). It makes more sense to call CTFs hackathons in my opinion but I digress. Whilst the culture of hackathons are not healthy, with free energy drinks, snacks and ridiculous staying all night culture. It is still great fun and enables individuals to learn a lot in a short amount of time (if done correctly). I've been to really bad hackathons and some amazing ones, but a great hackathon ensures there is proper food, support for individuals and a 🚬 area .

## Eth Oxford

The fortnight begins at [EthOxford](https://ethoxford.io/) I am currently working at a startup where we're building data analytics tools to web3 companies to provide data driven solutions. The larger goal is to provide full autonomy to DAOs. Check us out on [github](https://github.com/Lumous-Labs). So far we've built a data analytics to visualise community behaviours within discord servers, we are able to provide data driven insights into community to be able to identify "influencers". Our aim at this hackathon is to provide integration with github so we can provide the same features via aggregating discord and github data, this will enable us to identify "builders" a developer with strong social presence. Working with github's API was luckily not problematic however we were confronted with a major problem.

### Data pairing

A contingency associated with doing the builder analysis is to have pairing of discord accounts and github accounts. By pairing we can confidently state that these 2 accounts have the same owner. This was proven to be a challenge, since if this information was stored somewhere it will be in a highly unstructured area of the internet. From our analysis on the HomeDao Server we quickly realised that it was a rarity for people to link the github to their discord account. As you can see below.


![visualisation of accounts shared on discord](/images/discord_with_github.png)


So from a personal level we need to address if this a technical or a business problem. Never the less we cant solve this fancy problems at a hackathon so instead my team started manually asking people for this information. This is when we realised that most members who are part of the hackathon haven't joined the discord/hasn't messaged within the server. This makes our analytics kind of useless since there is little to no value we can equate with no activity. However luckily my team was persistent and we were able to reduce our initial list of 70 github and discord usernames to 25 ish. Another perk of manual data analysis we realised is the cleaning we needed to do. Most people gave us their display names and it there was small information missing from these names too, such as a hidden full stop or Capital letters. Never the less me and my team worked through all of the problems and finally had a [working demo](https://www.youtube.com/watch?v=zvvhJghXfzw).

### Judging

The juding experience was interesting we were given a room for our track (social/gaming) and we were told to wait. Our team was talking to other teams and we were asked to present. We presented second a friend of mine did a quick explanation tinkering with Farcaster, it wasn't a complete submission. Whilst going up to the stage I accidently palmed the drink of someone. It spilt a little bit and I expressed my sorry, later we found out that this [individual](https://a16zcrypto.com/team/jay-drain/) was the judge and representative of a16z crypto 💀. Our presentation went smoothly and answered 2 questions that came from the judge. My opinion on other individuals works were mixed. There was some clearly talented people, a lot of rushed project, some project that felt like the first [apple demo](https://www.reddit.com/r/technology/comments/18jyiks/steve_jobs_rigged_the_first_iphone_demo/) and some projects that blurred what they've built in the hackathon with past work.

In the end we didn't win the track but I thoroughly enjoyed working with the team and meeting people at the hackathon!

[FINAL SUBMISSION](https://taikai.network/home-dao/hackathons/ethoxford/projects/cltln8yo7057vw201xzhayuo9/idea)

## ETHGlobal London

Next week was [ETHGlobal london](https://ethglobal.com/showcase?events=london2024) During EthOxford I met some individuals who are very interested in FHE, this is a field that I've done research and built on before and I truly believe it can revolutionise the world. So for this hackathon I wanted to work on FHEVM which is an EVM application of FHE, I've heard of companies like Zama and Fhenix building on this and luckily Fhenix had a bounty for this hackathon. So our team of 4 went to the drawing board to start theorising potential applications. Working with a group of new individuals for the first time was intense. Understanding peoples way of working and aligning on a goal was hard to gauge.

### Ideas

FHE changes the mechanism of interacting with systems. Therefore it can be hard to understand where it provides strong utility when building on FHE, taking into consideration the computational overhead drastically restricts its application, but there are many companies working to [alleviate this issue](https://www.techrepublic.com/article/intel-innovation-fully-homomorphic-encryption/). We came finalised on 4 different ideas.

1. [FHE DRM](https://github.com/orgs/zama-ai/projects/27/views/1?pane=issue&itemId=52794552): this is a bounty on zama, so the aim will be to build it on Fhenix then convert the solution to Zama's FHEVM. However after spending some time on it as a team we didn't have a strong idea on how to implement this and wether it is feasible to finish it within the 36 hours.
2. FHE Linear Regression: as mentioned previously there are massive computational overhead, however FHE is in a great position to implement ML, this was a strong contender and had clear application of using healthcare data in a decentralised and anonymous way, however after speaking to the FHEnix team and assessing the computational feasibility we realised that we'd have to wrestle with the Fhenix EVM a lot to able to build and sustain a model. In the future I'd was in strong favour to work on this but at the current stage of the EVM it was not feasible due to computational overhead and the [threshold protocol](https://www.fhenix.io/cracking-the-code-overcoming-challenges-of-on-chain-fhe-part-1/) not being implemented.
3. FHE LP: This was a very interesting idea but in my opinion i think we didn't spend enough time to iron out the nuiances of what this will require. The order book is problematic since it's hard to decide what will be encrypted in the LP pool. For example to my understanding if the volume of the LP was encrypted getting quotes will be impossible since the ouput of the rates will be encrpyted. The same issue arrises for price and other elements of a LP.
4. FHE Gaming: Most gaming computation is low overhead and there's a strong element of doing computation on private data. There are [companies](https://www.tonk.gg/) providing this service to the blockchain and On chain gaming has always struggled to find it's footing, on of the reasons being private state. Some basic computation can be comparison checks, this can enable so much within gaming: think wordle,crossword and battle ships.

### BattleFHEps

After having a cigarette with a developer from CryptoKitty, we decided that sticking to the game battleships is feasible and more fun. It's a timeless classic. Developing it wasn't to problematic when it came to the smart contracts but there was some tooling on the FHEnix team that didn't work as expected. For example their gas estimation tooling was incorrect, for large computation for encrypted dataset. This was problematic to identify due to the nature of the problem since the transactions were "successfully failing" it did not help that the testnet and block explorer were also down during some periods of the hackathon.

Working with FHE was fun but identify appropiate usecases for FHEVM was more difficult than anticipated, the technology and research needs to mature a lot more to have more robust applications. The judging was fairly swift, we presented our application to the Fhenix Team, got a bunch of merch. In the end we weren't succesful with the bounty. But the individual who did get first place worked on a very interesting project, It was a ZK prover within FHEVM. He's working style really inspired me on how to approach hackathons in the future. He spent, the first 8 hours just writing the pure logic took a nap and spend the remaining time coding it. He definently deserved the prize.

[FINAL SUBMISSION](https://ethglobal.com/showcase/battlefheps-x90cc)

## What's next

I thoroughly enjoy hacking and building small projects, I learn so much and meet amazing people that I will be at more hackathons soon, there was an interesting opportunity to learn more about FHE at a castle in Germany!
