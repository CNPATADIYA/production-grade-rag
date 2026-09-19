from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()

def main():
    model = ChatOpenRouter(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        temperature=0.8,
    )

    # Example usage
    response = model.invoke("What is RAG ?")
    print(response.content)


if __name__=="__main__":
    main()