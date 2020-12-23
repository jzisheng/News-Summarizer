from transformers import AutoTokenizer, AutoModel,pipeline



classifier = pipeline('summarization')
text = '''
(CNN)For this week, we think about what justice might look like in the Breonna Taylor case, discuss great performances by the music icons Patti LaBelle and Gladys Knight, and revisit the horrifying history of forced sterilizations. Plus, recommendations: Esquire's profile of Michael Kenneth Williams and Hulu's "High Fidelity."

This week's culture conversation: Justice for Breonna Taylor?
Brandon: One of the biggest stories this week is the historic settlement in the Breonna Taylor case. On Tuesday, the city of Louisville, Kentucky, announced that it'd pay $12 million to Taylor's family.
Leah: What were your first thoughts when you heard the news?
B: The announcement was very, very moving. At the same time, like a lot of people, I had a reaction that I'll sum up as "great, but": The size of the settlement is great, very definitely, but what about the officers who were involved in the flawed raid that took Taylor's life?
Six months later, they still haven't been charged with a crime.
"It's time to move forward with the criminal charges, because she deserves that and much more," is how Taylor's mom put it.
L: Yeah, that's true. It's also the largest settlement ever paid by the city of Louisville, right? So off the bat, that was shocking to me, even though it took months of nationwide protests to get there. Right away, though, the sheer size of the sum -- and the fact that Taylor's family got a sizable settlement at all -- struck me.
B: I can sense a "but" coming ...
L: You're not wrong! BUT: At the end of the day, the money isn't the most important part of the case. The money is just a bandage. It can't address the underlying illness of police violence.
B: Which is why something else also jumped out at me: the promise to institute police reforms. The city agreed to offer a housing program to incentivize officers to live in the areas where they serve, involve social workers when appropriate and tighten the process of how search warrants are issued.
All that's important, too, I think.
L: Yes! Taylor's mom touched on the role of the reforms: "Justice for Breonna means that we will continue to save lives in her honor. No amount of money accomplishes that, but the police reform measures that we were able to get passed as a part of this settlement mean so much more to my family, our community and to Breonna's legacy."
B: That, to me, is the takeaway: The settlement is a big step, but it's still just one step on a longer path to justice.
'''
res = classifier(text)
print(res)
