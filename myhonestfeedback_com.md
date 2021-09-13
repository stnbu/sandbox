# My (Totally) Honest Feedback dot Com

The domain name is registered to a totally-not-squatter. But it needn't be so on the nose anyhow, eh Twitter?

## The Idea in URLs

`bob`: The username of a user that has an account

---

### POST `https://myhonestfeedback.com/bob/haircut/new` (as anon)

Body:

```
Bro, Robert, you need to get a haircut. People around the office are starting to call you "Porno Bob".
```

Someone anonymously gives bob feedback on his haircut. The `/haircut/` slug needn't exist in advance (or do it?)

---

### PUT `https://myhonestfeedback.com/bob/drunken-office-christmas-party` (as `bob`)

Body:

```
Um. I had a lot to drink, didn't I. Was great seeing the whole team together like that. Feel free to drop me social etiquette tips of any kind here.
```

Bob creates the `drunken-office-christmas-party` url slug, explaining what he wants feedback about.
*

---

### POST `https://myhonestfeedback.com/bob/drunken-office-christmas-party/publish` (as `bob`)

Bob decides to air the whole embarrassing mess to anyone anywhere, and replies to some feedback with comments and apologies (probably).

---

### POST `https://myhonestfeedback.com/bob/haircut/01234/respond` (as `bob`)

Body:

```
Oh. Heh. Wowzers. I thought this was the style at this time. I'll get right on that anon. Thanks.
```

Bob responds to a particular piece of nasty haircut commentary.

---

### GET `https://myhonestfeedback.com/bob` (as anon)

Responds with Bob's "dashboard" of whatever kind. Probably whatever he wants to publish, whatever you can see as anon.

Probably would be best to not let `bob` have any special permissions with regard to `alice`. If someone posts some feedback about `user_x`, they are _always_ anonymous, even if they are logged in to the site as `user_x`.
