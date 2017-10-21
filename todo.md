## Notes/resources
- https://developer.amazon.com/docs/custom-skills/steps-to-build-a-custom-skill.html
- https://developer.amazon.com/docs/ask-overviews/understanding-how-users-interact-with-skills.html
- https://developer.amazon.com/docs/custom-skills/use-the-skill-builder-beta-to-define-intents-slots-and-dialogs.html

## Todo
- [ ] write interaction model
  - [x] needs unique invocation name ("fortune" is probably taken)
- [ ] write py to parse fortune file
  - [ ] may import to db/dynamo db, but dynamo dones't have built in support for random access
  - [ ] uses strfile format for quicker random access: https://linux.die.net/man/1/strfile
- [ ] write py for skill (started sample)
