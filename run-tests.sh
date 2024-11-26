if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed!"
    echo "Please install Docker Desktop for Mac first."
    exit 1
fi

if ! docker info &> /dev/null; then
    echo "Error: Docker is not running!"
    echo "Please start Docker Desktop for Mac."
    exit 1
fi

if [ ! -f .env ]; then
    echo "Error: .env file not found!"
    echo "Please create .env file with NASA_API=DEMO_KEY"
    exit 1
fi

if [ -z "$(grep NASA_API= .env | cut -d '=' -f2)" ]; then
    echo "Error: NASA_API key is not set in .env file!"
    echo "Please add NASA_API=DEMO_KEY to .env file"
    exit 1
fi

mkdir -p reports

echo "Starting NASA API tests..."

export $(cat .env | xargs)

docker-compose up --build

if [ $? -eq 0 ]; then 
    echo "Tests completed successfully!"
    echo "Check reports directory for test results."
else
    echo "Tests failed!"
    exit 1
fi