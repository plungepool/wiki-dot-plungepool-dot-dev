# audio engineering.

Miscellanous advice I often find myself giving, compiled at last.

## mixing.

### how to take mix notes.

Feedback is an important part of the process of mixing. Audio engineering is first and foremost a service industry. Much like other creative work it's not supposed to be perfect the first try, though a good mixer can come close enough so that mix notes consist of smaller adjustments, leading to a better overall product.

The quickest way to know if something will work is just to try it, and even if you don't think something's going to work, doing it anyway for your client will dispel any questions, and best case you might be pleasantly surprised with the result.

Don't make excuses or qualifications for what you did when sending a mix unless you have to. Conveying uncertainty about the strength of a decision you made before a mix is even heard serves only to put your client on high alert and breeds second-guessing and mistrust. Stand by your work, and let your client tell you what to make better.

Always buy into the notion that your client's notes are beneficial to the mix. It's their record, not yours.

### how to give mix notes.

When possible, try to avoid audio terms that are ambigious, even if they are common. Terms like "muddy," "thin," "bright," and "dark," all require further clarificiation. Always specify what the problem instruments are, and the effect you hope to hear by adjusting them such as "making the bass guitar more defined" or "making the overall sound less harsh when listening with the volume way up."

When possible, describe the problem to be solved without prescribing the solution. Instead of saying "boost the high-end in the chorus" say something like "the chorus is feeling a bit dull to me, can we make it sound more exciting?" If you are sure that your prescribed solution will help, feel free to include it as long as you are also describing the desired effect of the change.

Failing to state the problem to be solved while prescribing the solution means the engineer must make the change blindly without being able to judge whether or not the change they made has met its goal. Even worse, they may assume your intentions to be something completely different like "maybe they are hoping to hear the cymbals more clearly" or  "maybe they think the chorus is too bass-forward." If they attempt to carry out your solution and it doesn’t have the desired effect, it can produce frustration on both sides when it feels like they can't understand what you mean, while they may feel like you don't know what you want.

Always share your vision with your engineer. This helps them to come up with effective solutions to creative problems. Sharing reference songs and your own rough mixes are a great start.

## mastering.

### making your song loud.

I made this half-hour long video about the percieved loudness of a song goes far beyond dynamic range and compression. The reasons may surprise you!

<iframe width="560" height="315" src="https://www.youtube.com/embed/MBQ_rBcNnN4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Accompanying this video I recommend reading [one of the best posts about mastering ever made on Gearspace.com](https://gearspace.com/board/mastering-forum/1252522-targeting-mastering-loudness-streaming-lufs-spotify-youtube-why-not-do.html), which is imporant enough that I have chosen to mirror it  (pre-2021 update) below. 

> Regarding mastering to streaming LUFS loudness normalization targets - I do not recommend trying to do that. I know it's discussed all over the web, but in reality very few people actually do it. To test this, try turning loudness matching off in Spotify settings, then check out the tracks listed under "New Releases" and see if you can find material that's not mastered to modern loudness for it's genre. You will probably find little to none. Here's why people aren't doing it:
>
> 1 - In the real world, loudness normalization is not always engaged. For example, Spotify Web Player and Spotify apps integrated into third-party devices (such as speakers and TVs) don’t currently use loudness normalization. And some listeners may have it switched off in their apps. If it's off then your track will sound much softer than most other tracks.
>
> 2- Even with loudness normalization turned on, many people have reported that their softer masters sound quieter than loud masters when streamed.
>
> 3 - Each streaming service has a different loudness target and there's no guarantee that they won't change their loudness targets in the future. For example, Spotify lowered their loudness target by 3dB in 2017. Also, now in Spotify Premium app settings you find 3 different loudness settings; "Quiet, Normal, and Loud". It's a moving target. How do the various loudness options differ? - The Spotify Community
>
> 4 - Most of the streaming services don't even use LUFS to measure loudness in their algorithms. Many use "ReplayGain" or their own unique formula. Tidal is the only one that uses LUFS, so using a LUFS meter to try to match the loudness targets of most of the services is guesswork. Edit: In September 2019 YouTube switched to -14 LUFS. In December 2020 Spotify began transitioning from "ReplayGain+3dB" to -14 LUFS. It's good that a normalization standard is emerging. It's also more evidence that they can change these targets at any time.
>
> 5 - If you happen to undershoot their loudness target, some of the streaming sites (Spotify, for one) will apply their own limiter to your track in order to raise the level without causing clipping. You might prefer to have your mastering engineer handle the limiting.
>
> 6 - Digital aggregators (CD Baby, TuneCore, etc.) generally do not allow more than one version of each song per submission, so if you want a loud master for your CD/downloads but a softer master for streaming then you have to make a separate submission altogether. If you did do that it would become confusing to keep track of the different versions (would they each need different ISRC codes?).
>
> It has become fashionable to post online about targeting -14LUFS or so, but in my opinion, if you care about sounding approximately as loud as other artists, and until loudness normalization improves and becomes universally implemented, that is mostly well-meaning internet chatter, not good practical advice. My advice is to make one digital master that sounds good, is not overly crushed for loudness, and use it for everything. Let the various streaming sites normalize it as they wish. It will still sound just as good.

### on gapless playback.

Gapless playback has died, the streaming paradigm killed it, and most people didn't even notice it was taken from them.

Apple proports to still support it as a feature but breaks it constantly across all of their devices. Most streaming service and music players do not provide the option without adding an artificial crossfade.

Music players and streaming services may add a gap between tracks on playback due to bandwidth latency, and when those tracks mastered to play perfectly seamlessly together without gaps it can create a "popping" sound at the sample level since a waveform is being cut off, which is one reason not to leave things up to chance by seperating tracks like this without using fades.

When a client asks you to master songs together with gapless in mind, you essentially have two options:

1. Embrace the gap. Assume a gap on playback on basically every streaming service and add a small few millisecond fade that may or may not be noticeable in a true gapless playback environment, which you can check if you want. By controlling how the track transitions yourself you're creating more predictability for how it will play across all environments, which is my personal preference. If you're targeting for vinyl/cassette you could export a separate side A/side B master without gaps for those, or for CD take your chances without a fade since CD players are more likely to play back gapless.
2. Cut and seperate tracks with no fade and risk a popping between tracks on playback. Some music players and streaming services sometimes add in a small fade themselves if there is a risk of popping, but it isn't guaranteed. If you're worried about a pop being produced you can try testing it yourself, but again every service and music player will handle it differently. You may still decide to go this route because it's potentially more "future-proof" and would play well in a theoretical future where streaming services decide to embrace gapless, but there's no guarantee of that ever happening.