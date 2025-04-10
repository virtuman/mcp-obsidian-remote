from . import server

def main():
    """Main entry point for the package."""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(
        description="MCP server to work with Obsidian remotely via REST plugin"
    )
    # Add arguments if needed
    parser.add_argument("--transport", type=str, help="sse or stdio")

    args = parser.parse_args()
    # asyncio.run(server.main())  # Rename current main to main_async
    server.main(transport=args.transport)  # Rename current main to main_async

if __name__ == "__main__":
    main()
