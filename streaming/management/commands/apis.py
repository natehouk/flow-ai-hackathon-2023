from apscheduler.schedulers.background import BackgroundScheduler
from streaming.management.commands.newsfeed import request_headlines
from streaming.models import Data, Summaries, DataAPIs, SummariesAPIs
from streaming.management.commands.chatgpt import get_prompt
import ast

class CustomInstanceAPIs():
    def __init__(self,source):
        self.status = False
        self.source = source
        self.previousheadlines = []
        self.updateed_idx = 0
        self.chat_gpt_start_idx = -1
        self.chat_gpt_end_idx = 0
        self.send_to_chat_gpt = False


    def add_data_to_model(self,):
        if self.source == "news":
            # headlines = request_headlines(set(self.previousheadlines))
            headlines = ["{'title': 'Cracker Barrel refuses to axe Pride Month support despite deluge of bigoted attacks - The Independent', 'description': 'Cracker Barrel has moved towards inclusivity and diversity over the years', 'source': 'Independent'}", '{\'title\': "What\'s being built in generative AI today? - TechCrunch", \'description\': "If you look past the headlines about the money and hype around generative AI, what are today\'s AI startups building?", \'source\': \'TechCrunch\'}', '{\'title\': \'Apple, Amazon must face consumer lawsuit over iPhone, iPad prices, US judge rules - Reuters\', \'description\': \'Apple <a href="https://www.reuters.com/companies/AAPL.O/"target="_blank">(AAPL.O)</a> and Amazon.com <a href="https://www.reuters.com/companies/AMZN.O/"target="_blank">(AMZN.O)</a> must face a consumer antitrust lawsuit in U.S. court accusing them of conspiri…\', \'source\': \'Reuters\'}', '{\'title\': "Dow Jones Pares Gains At Midday. Tesla Charges Higher On GM News, While Adobe Jumps Ahead Of Earnings. - Investor\'s Business Daily", \'description\': "The Dow Jones fell off highs near midday Friday, but Salesforce held a solid gain and Adobe gapped up ahead of next week\'s earnings report.", \'source\': "Investor\'s Business Daily"}', '{\'title\': \'Tesla jumps as GM deal makes its charging network closer to US standard - Reuters\', \'description\': \'Tesla <a href="https://www.reuters.com/companies/TSLA.O/"target="_blank">(TSLA.O)</a> shares closed 4% higher on Friday after General Motors <a href="https://www.reuters.com/companies/GM.N/"target="_blank">(GM.N)</a> joined Ford <a href="https://www.reuters.c…\', \'source\': \'Reuters\'}', '{\'title\': "Reddit won\'t budge on the API changes that are shutting down apps like Apollo - The Verge", \'description\': \'Based on comments from Reddit CEO Steve Huffman in an AMA, it doesn’t seem like the company will be budging on its controversial API changes.\', \'source\': \'The Verge\'}', "{'title': 'Feds charge two men for the $400 million Bitcoin hack that took down Mt. Gox - The Verge', 'description': 'The Department of Justice is charging two Russian nationals for their role in the hacks that brought down the now-defunct Mt. Gox Bitcoin exchange.', 'source': 'The Verge'}", "{'title': 'Moving from NY to Miami can save $195K in cost of living, taxes - New York Post ', 'description': 'New Yorkers making could save up to $200,000 in taxes by moving from Manhattan — where the overhead is 137% above the US average — to Miami, where costs are only 22.8% above the average…', 'source': 'New York Post'}", "{'title': 'Binance and Coinbase: Experts Weigh What’s Coming Next - CoinDesk', 'description': 'Will the SEC win? Will Binance close in the U.S.? What will Congress do? As the SEC launches wide-ranging suits against crypto’s biggest players, we asked a range of experts to peer into the future.', 'source': 'CoinDesk'}", '{\'title\': \'S&P 500 finishes week at highest level since August, as Nasdaq logs 7th-straight winning week: Stock market news today - Yahoo Finance\', \'description\': "Stocks popped on Friday after the S&P 500 officially entered a bull market to end Thursday\'s trading session.", \'source\': \'Yahoo Entertainment\'}', '{\'title\': \'2025 Volvo EX30: 10 Weirdest Interior, Exterior Design Details - Jalopnik\', \'description\': "The $35,000 EX30 is reasonably priced for an EV — especially a Volvo EV. It\'s also full of clever and cost-conscious design ideas.", \'source\': \'Jalopnik\'}', "{'title': 'Stock market could resume its downward spiral soon, Wall Street veteran warns - Fox Business', 'description': 'Wall Street veteran James Demmert warned the bear market is not yet over despite a months-long rally, and said stocks could tumble another 10% this year.', 'source': 'Fox Business'}", '{\'title\': \'Netflix sign-ups jump as U.S. password sharing crackdown kicks off - Reuters\', \'description\': \'Daily U.S. sign-ups for Netflix <a href="https://www.reuters.com/companies/NFLX.O/"target="_blank">(NFLX.O)</a> have jumped in the first few days after the streaming giant\\\'s password-sharing crackdown came into effect on May 23, data from research firm Antenn…\', \'source\': \'Reuters\'}', "{'title': 'The New Lexus GX Cashes In On The Overlanding Thing With Overtrail Model - Jalopnik', 'description': 'The 2024 Lexus GX 550 is in the running for best off-road SUV, but the new model is also leaning into the overlanding fever in the U.S.', 'source': 'Jalopnik'}", "{'title': 'Tesla looks to expand 4680 cell production with new Fremont facility - TESLARATI', 'description': 'Tesla is expanding its business in Fremont, California, with a new facility that will be responsible for helping ramp 4680 cell production.', 'source': 'Teslarati'}", '{\'title\': "JPMorgan\'s Jamie Dimon sought for second interview in Jeffrey Epstein lawsuit - Financial Times", \'description\': \'Lawyers for woman suing over bank’s ties to the late sex offender have questions about new documents\', \'source\': \'Financial Times\'}', '{\'title\': "CRSP Stock Pops As FDA Sets December Data To Potentially OK Gene-Editing Drug | Investor\'s Business Daily - Investor\'s Business Daily", \'description\': "The agency said it will make an approval decision on Crispr\'s exa-cel in December.", \'source\': "Investor\'s Business Daily"}', "{'title': 'Layoffs hit Colorado space companies Ursa Major, Orbit Fab - CNBC', 'description': 'The layoffs came at Ursa Major, which makes rocket engines, and Orbit Fab, a startup aiming to provide refueling services to spacecraft.', 'source': 'CNBC'}", "{'title': 'JPMorgan bond chief Bob Michele sees worrying echoes of 2008 in market calm - CNBC', 'description': 'Economic crosscurrents have divided the investing world into roughly two camps: Those who see a soft landing and those who envision something far worse.', 'source': 'CNBC'}", "{'title': 'Crypto.com suspends US institutional exchange service - Cointelegraph', 'description': 'Crypto .com will suspend its U.S. institutional cryptocurrency exchange offering due to poor demand under tough market conditions.', 'source': 'Cointelegraph'}"]
            curr_length = len(self.previousheadlines)
            for headline in headlines:
                curr_headline = ast.literal_eval(headline)
                if curr_length >= 1000:
                    self.previousheadlines.pop(0)
                curr_length += 1
                self.previousheadlines.append(headline)
                DataAPIs.objects.create(source=curr_headline["source"],description=curr_headline["description"],title=curr_headline["title"])
                self.chat_gpt_end_idx += 1
            if len(headlines) != 0:
                self.send_to_chat_gpt = True



    def chat_gpt_integration(self,):
        if self.source == "news":
            if not DataAPIs.objects.last().update:
                return 
            if self.send_to_chat_gpt:
                objects = DataAPIs.objects.filter(id__gt=self.chat_gpt_start_idx, id__lte=self.chat_gpt_end_idx)
                prompt = ""
                for inst_object in objects:
                    prompt += f"{inst_object.description} "
                text = get_prompt(prompt)

                if text != False:
                    SummariesAPIs.objects.create(value=text,update=False)
                self.chat_gpt_start_idx = self.chat_gpt_end_idx
                self.send_to_chat_gpt = False

    def run(self,):
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.add_data_to_model)  # Adjust the interval as needed
        self.scheduler.start()

        self.scheduler2 = BackgroundScheduler()
        self.scheduler2.add_job(self.chat_gpt_integration,  'interval', seconds=2)  # Adjust the interval as needed
        self.scheduler2.start()

        try:
            # This is needed to keep the main thread alive
            # so the background scheduler can continue running
            while True:
                if self.status:
                    self.scheduler2.shutdown()
                    self.scheduler.shutdown()
                    # print("youtube stopped")

                    break
        except KeyboardInterrupt:
            # scheduler.shutdown()
            self.scheduler2.shutdown()
            self.scheduler.shutdown()
