# Use Maven with Java 17 to build the application
FROM maven:3.8.5-openjdk-17 AS builder

WORKDIR /app
COPY pom.xml .
COPY src ./src

# Build the application with Java 17
RUN mvn clean package -DskipTests

# Use Amazon Corretto 17 for runtime (application will run with Java 17)
FROM amazoncorretto:17

WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar

ENTRYPOINT ["java", "-jar", "app.jar"]