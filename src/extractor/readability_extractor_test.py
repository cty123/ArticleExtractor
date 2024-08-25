import unittest
from unittest.mock import Mock, MagicMock
from src.extractor.readability_extractor import ImageContent, ReadabilityExtractor, TextContent

RAW_TEXT = """
<div id="readability-page-1" class="page">
    <article>
        <figure>
            <div data-component="image-block">
                <p><img src="/bbcx/grey-placeholder.png"><img
                        sizes="(min-width: 1280px) 50vw, (min-width: 1008px) 66vw, 96vw"
                        srcset="https://ichef.bbci.co.uk/news/240/cpsprodpb/6e22/live/305f3e80-5ce1-11ef-ad2e-252430c5dda7.png.webp 240w,https://ichef.bbci.co.uk/news/320/cpsprodpb/6e22/live/305f3e80-5ce1-11ef-ad2e-252430c5dda7.png.webp 320w,https://ichef.bbci.co.uk/news/480/cpsprodpb/6e22/live/305f3e80-5ce1-11ef-ad2e-252430c5dda7.png.webp 480w,https://ichef.bbci.co.uk/news/640/cpsprodpb/6e22/live/305f3e80-5ce1-11ef-ad2e-252430c5dda7.png.webp 640w,https://ichef.bbci.co.uk/news/800/cpsprodpb/6e22/live/305f3e80-5ce1-11ef-ad2e-252430c5dda7.png.webp 800w,https://ichef.bbci.co.uk/news/1024/cpsprodpb/6e22/live/305f3e80-5ce1-11ef-ad2e-252430c5dda7.png.webp 1024w,https://ichef.bbci.co.uk/news/1536/cpsprodpb/6e22/live/305f3e80-5ce1-11ef-ad2e-252430c5dda7.png.webp 1536w"
                        src="https://ichef.bbci.co.uk/news/480/cpsprodpb/6e22/live/305f3e80-5ce1-11ef-ad2e-252430c5dda7.png.webp"
                        loading="eager" alt="BBC Vice-President Kamala Harris"><span>BBC</span></p>
            </div>
        </figure>
        <div data-component="text-block">
            <p>When Kamala Harris steps onto the stage at the Democratic National Convention in Chicago this week as the
                party’s presidential nominee, she’ll do so knowing that many in the audience cheering her on once
                counted her out.<!-- --></p>
            <p>Ms Harris, 59, has faced years of doubt from some within her party about her ability to run for America’s
                highest political office - including from President Joe Biden, the man whom she continues to serve as
                vice-president.<!-- --></p>
            <p>Since replacing Mr Biden as Democratic nominee in mid-July, Ms Harris has seen a tidal wave of enthusiasm
                for her candidacy - reflected in polling, fundraising and the enormous crowds that have come out to see
                her at rallies across the country.<!-- --></p>
            <p>But the political momentum and energy she has generated in recent weeks among Democrats was never a
                given.<!-- --></p>
            <p>After failing in a short-lived presidential bid in 2019, she began her vice-presidency on a shaky
                footing, beset by stumbles in high-profile interviews, staff turnover and low approval ratings. And for
                the last three-and-a-half years in the White House she has struggled to break through to American
                voters.<!-- --></p>
            <p>Advisers and allies say that in the years since those early struggles she has sharpened her political
                skills, created loyal coalitions within her party and built credibility on issues like abortion rights
                that energise the Democratic base. She has, in other words, been preparing for a moment exactly like
                this one.<!-- --></p>
            <p>On Thursday, as she formally accepts the Democratic nomination, Ms Harris has an opportunity to
                reintroduce herself on the national stage with fewer than 80 days until an election that could see her
                become the nation’s first female president.<!-- --></p>
            <p>At the same time, she’ll have to prove that she is capable of leading a party that never saw her as its
                natural leader and remains divided over the war in Israel and Gaza.<!-- --></p>
            <p>But above all, she’ll need put to rest any lingering doubt among the Democratic faithful that she can
                meet the challenge of defeating former president Donald Trump in what remains a tight and unpredictable
                contest.<!-- --></p>
        </div>
        <figure>
            <div data-component="image-block">
                <p><img src="/bbcx/grey-placeholder.png"><img
                        sizes="(min-width: 1280px) 50vw, (min-width: 1008px) 66vw, 96vw"
                        srcset="https://ichef.bbci.co.uk/news/240/cpsprodpb/e87f/live/f08bfaf0-5ce0-11ef-b43e-6916dcba5cbf.png.webp 240w,https://ichef.bbci.co.uk/news/320/cpsprodpb/e87f/live/f08bfaf0-5ce0-11ef-b43e-6916dcba5cbf.png.webp 320w,https://ichef.bbci.co.uk/news/480/cpsprodpb/e87f/live/f08bfaf0-5ce0-11ef-b43e-6916dcba5cbf.png.webp 480w,https://ichef.bbci.co.uk/news/640/cpsprodpb/e87f/live/f08bfaf0-5ce0-11ef-b43e-6916dcba5cbf.png.webp 640w,https://ichef.bbci.co.uk/news/800/cpsprodpb/e87f/live/f08bfaf0-5ce0-11ef-b43e-6916dcba5cbf.png.webp 800w,https://ichef.bbci.co.uk/news/1024/cpsprodpb/e87f/live/f08bfaf0-5ce0-11ef-b43e-6916dcba5cbf.png.webp 1024w,https://ichef.bbci.co.uk/news/1536/cpsprodpb/e87f/live/f08bfaf0-5ce0-11ef-b43e-6916dcba5cbf.png.webp 1536w"
                        src="https://ichef.bbci.co.uk/news/480/cpsprodpb/e87f/live/f08bfaf0-5ce0-11ef-b43e-6916dcba5cbf.png.webp"
                        loading="lazy" alt="Kamala Harris "></p>
            </div>
        </figure>
        <p data-component="subheadline-block">
        <h2>Path to the White House <!-- --></h2>
        </p>
    </article>
</div>
"""


class TestExtractor(unittest.TestCase):

    def test_extract_dom(self):
        # Given & When
        extractor = ReadabilityExtractor()
        extracted_contents = extractor.analyze_content(RAW_TEXT)

        # Then
        self.assertEqual(5, len(extracted_contents))
        self.assertIsInstance(extracted_contents[0], ImageContent)
        self.assertEqual('/bbcx/grey-placeholder.png',
                         extracted_contents[0].src)
        self.assertIsInstance(extracted_contents[1], ImageContent)
        self.assertEqual(
            'https://ichef.bbci.co.uk/news/480/cpsprodpb/6e22/live/305f3e80-5ce1-11ef-ad2e-252430c5dda7.png.webp',
            extracted_contents[1].src)
        self.assertIsInstance(extracted_contents[2], TextContent)
        self.assertEqual(9, len(extracted_contents[2].paragraphs))


if __name__ == "__main__":
    unittest.main()
