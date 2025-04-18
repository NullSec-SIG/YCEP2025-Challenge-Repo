# Use the official .NET SDK image to build and run the application
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env

# Set the working directory
WORKDIR /app

# Copy the C# project file and restore any dependencies
COPY *.csproj ./
RUN dotnet restore

# Copy the rest of the application source code
COPY . ./

# Build the application
RUN dotnet publish -c Release -o out

# Use a runtime image to run the application
FROM mcr.microsoft.com/dotnet/aspnet:6.0

# Set the working directory in the runtime image
WORKDIR /app

# Copy the built application from the build environment
COPY --from=build-env /app/out .

# Copy the source code from the build environment to the runtime image
COPY --from=build-env /app/flag.txt .

RUN ["apt", "update"]

RUN ["apt", "install", "socat", "-y"]

# Expose the port that your application runs on
EXPOSE 2403

# Run the application
ENTRYPOINT ["socat", "TCP-LISTEN:2403,reuseaddr,fork", "EXEC:dotnet LionExchange1.dll"]