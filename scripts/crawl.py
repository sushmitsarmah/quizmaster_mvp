import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def main():
    # Configure the browser
    browser_config = BrowserConfig(
        headless=True,  # Set to False so you can see what's happening
        verbose=True,
        user_agent_mode="random",
        use_managed_browser=True, # Enables persistent browser sessions
        browser_type="chromium",
        user_data_dir="./user_data"
    )

    # Set crawl configuration
    crawl_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        markdown_generator=DefaultMarkdownGenerator()
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://crypto.news/",
            config=crawl_config
        )

        if result.success:
            print("Raw Markdown Length:", len(result.markdown_v2.raw_markdown))
            print("Citations Markdown Length:", len(result.markdown_v2.markdown_with_citations))

if __name__ == "__main__":
    asyncio.run(main())
