def run_app():
    print("here we go")


if __name__ == "__main__":
    try:
        run_app()
    except Exception as error:
        print(f"Something went wrong {error}")