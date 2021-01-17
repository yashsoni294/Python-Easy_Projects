import re
string="""
Don’t miss what’s happening
People on Twitter are the first to know.
Soumyo Roy
3,502 Tweets
See new Tweets
Soumyo Roy
@soumyo_trader
Trader - Lifestyle Vlogger - Philanthropist - Financial Advisor 
DM to get the chance to join my Closed Signal Group.
bit.ly/thesorotradertwJoined August 2018
14 Following
54K Followers
Tweets
Tweets & replies
Media
Likes
Soumyo Roy’s Tweets
Soumyo Roy
@soumyo_trader
·
5 Jan
Good Afternoon Guys!!

We had a decent profit in today's afternoon session.

Please feel free to reach out to me for any queries related to Trading.
yashmukeshsoni@gmail.com

For new registration kindly 0701ce181032@uecu.ac.in click the link Down pointing backhand index
https://bit.ly/thesorotradertw

White heavy check markTrades:5+/1-
Banknote with dollar signProfit +474$

Small 0701ce181031@uecu.ac.in blue diamondWe'll begin at Wristwatch17:00 Hrs
Soumyo Roy
@soumyo_trader
·
5 Jan
7 Daily habits that changed my life:

Read
Write
Smile
Exercise
Practice gratitude
Say thank you sincerely
Call people by their first name.
0701ce181001@uecu.ac.in

We will be having the second session of the day at 13:00 Clock face five oclock hrs
Soumyo Roy
@soumyo_trader
·
5 Jan
Trading doesn't solve your money problems—it 0701ce181002@uecu.ac.in amplifies it.

HOW ARE YOU GUYS DOING?

We will begin our trading session at 13:00 Hrs.

See you there, good day doston.
Soumyo Roy
@soumyo_trader
·
5 Jan
Right-pointing double triangleChallenge yourself to rise above the fears that hold you back from achieving your goals. 

Heavy check markJoin my closed trading group today

Write to me here now... Send me a direct message Thumbs up
Soumyo Roy
@soumyo_trader
·
4 Jan
12 Important things schools don't teach:

Selling

Integrity

Adaptability

Reiterations
yashsoni@gmail.com

Embracing risk

Process > Results

Embracing failure

Financial education
ajayjadhav1999@gmail.com

Delayed gratification

Embracing grey areas

Thinking in probabilities

We will begin our afternoon at 1 PM sharp
Soumyo Roy
@soumyo_trader
·
4 Jan
tock trading tips:

1) Buy only when the overall market is in an uptrend

2) Focus on the strongest stocks

3) Avoid stocks that gapped more than 20% over the last 3 months

4) Ride your winners

5) Simple entry trigger—no need for complexity when you have nailed #1 to #4
Soumyo Roy
@soumyo_trader
·
4 Jan
Right-pointing double triangle"Behind every successful person, there are a lot of unsuccessful years."

Heavy check markJoin my closed trading group today 

The New Year Bringd in New opportunities. Lets try to make a head startThumbs up

DM me to join my closed group
Soumyo Roy
@soumyo_trader
·
3 Jan
In business:

You need capital.

You got expenses to cover.

You don't expect to succeed from day one.

You need some time before you make a profit.

Trading is a business—so treat it as one.
Soumyo Roy
@soumyo_trader
·
1 Jan
Wishing you all a very “Happy New Year 2021”

May this year bring new happiness, new goals, new achievements, and many new inspirations to your life. 

Wishing you a year fully loaded with happiness. 

I hope that this new year will be the best year of your life.
Soumyo Roy
@soumyo_trader
·
31 Dec 2020
Wishing all of you a very happening new year in advance. It's time to rejoice and celebrate with friends and family.

It's the time for cherishing relationships and to thank the Lord for protecting us during the pandemic.

Love you all doston.
Soumyo Roy
@soumyo_trader
·
31 Dec 2020
Right-pointing double triangleDon't let failure stop you from moving forward.

Heavy check markJust a friendly reminder to keep pushing forward, stay on track, and be positive. 

Right pointing backhand indexDM me to join my closed trading group today..
Soumyo Roy
@soumyo_trader
·
30 Dec 2020
Good Afternoon Friends!

We had an excellent profit today even after the constant market volatility.

I want all of you to predict the market the way I do.

For queries please DM.

See you in the evening at 5 PM with the second session of today.

White heavy check markTrades: 6+/2
Banknote with dollar signProfit +538$

Folded hands
Search Twitter
New to Twitter?
Sign up now to get your own personalized timeline!
You might like
Rajaršhì?a Electric light bulbChart with upwards trendChart with downwards trend
@RajarshitaS
Gautam Singhania
@SinghaniaGautam
Kiran Mazumdar-Shaw
@kiranshaw
Show more
Trending now
What’s happening
COVID-19
·
LIVE
COVID-19 in India
Entertainment
·
Last night
The teaser of Yash's KGF Chapter 2 is here
Trending with #HappyBirthdayYash
Trending in India
Signal
121K Tweets
Trending in India
#SurbhiJyoti
Trending with #KaranSinghGrover, #QuboolHai2Point0
US elections
·
Last night
Police officer among five dead after pro-Trump mob storms US Capitol
Show more
Terms of Service
Privacy Policy
Cookie Policy
Ads info
More
© 2021 Twitter, Inc."""
# pattern = re.compile(r'@gmail.com|@uecu.ac.in')
email_list = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",string)
for email in email_list:
    print(email)
print(email_list)
