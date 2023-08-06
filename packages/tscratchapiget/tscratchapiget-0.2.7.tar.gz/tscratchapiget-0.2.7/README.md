This project gets the scratch api. Everything in this project code by me (except some needed library). Big credit to TimMcCool(Scratcher) for example codes.

This can do:
    User features(v0.2.5 to v0.2.7):
        - Get a user unread-message-count ```message_count('[user]')```     EX: ```user.message_count('TimMcCool')```
        - Get a user id ```id('[user]')```     EX: ```user.id('griffpatch')```
        - Get if a user is a scratchteam ```scratchteam('[user]')```     EX: ```user.scratchteam('ScratchCat')``` #Return 'True'
        - Get user join date ```join('[user]')```     EX: ```user.join('Will_Wam')```#Return '2013-11-25T19:52:29.000Z'
        - Get a user pfp(link) ```pfp_link('[user]')```     EX: ```user.pfp_link('Scratch_Tony_14261')```          +Bonus Feature: Open that pfp link in browser. Change that to ```pfp_link_open('[Username]')```
        - Get user About-Me section ```aboutme('[user]')``` EX: ```user.aboutme('WazzoTV')```
        - Get user What-I'm-Working-On section ```wiwo('[username]')```     EX: ```user.wiwo('ceebee')```
        - Get user country ```country(['user]')```     EX: ```user.country(['')```
        - Get user follower count ```followers('[user]')```     Ex: ```user.followers('sharkyshar')```
        - Get user following count ```following('[user]')```     EX: ```user.followers('atomicmagicnumber')```