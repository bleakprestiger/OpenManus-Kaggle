#Generated Code By Gemma 3 --- NEW CODE
import asyncio
import argparse
from app.agent.manus import Manus
from app.logger import logger


async def main():
    """
    Main function to handle user prompts and process them using the Manus agent.
    It supports both interactive mode (prompt from user input) and command-line argument mode (prompt from
    --prompt or -p).
    """
    parser = argparse.ArgumentParser(
        description="Process prompts using the Manus agent."
    )
    parser.add_argument("--prompt", "-p", type=str, help="The prompt to process.")
    args = parser.parse_args()
    agent = Manus()
    try:
        if args.prompt:
            # Use the prompt provided as a command-line argument
            prompt = args.prompt
            logger.info("Prompt received from command line argument.")
        else:
            # Use the prompt provided by user input
            prompt = input("Enter your prompt: ")
            if not prompt.strip():
                logger.warning("Empty prompt provided.")
                return
        logger.info("Prompt received from user input.")
        logger.warning("Processing your request...")
        await agent.run(prompt)  # Run the agent's run method within an asyncio event loop.
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
