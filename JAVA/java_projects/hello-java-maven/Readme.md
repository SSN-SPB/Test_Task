# Hello Java Maven

A minimal Java project using Maven.

## Requirements

- Java JDK 21 (or newer)
- Apache Maven 3.9+

---

# 1. Install Java

## Windows

Download and install:

https://adoptium.net/

Choose:

- Eclipse Temurin JDK 21 (LTS)

Verify installation:

```bash
java -version
javac -version
```

---

## macOS

Using Homebrew:

```bash
brew install openjdk@21
```

Verify:

```bash
java -version
javac -version
```

---

## Ubuntu / Debian

```bash
sudo apt update
sudo apt install openjdk-21-jdk
```

Verify:

```bash
java -version
javac -version
```

---

# 2. Install Maven

## Windows

Download:

https://maven.apache.org/download.cgi

Extract Maven and add its `bin` directory to your PATH.

Verify:

```bash
mvn -version
```

---

## macOS

```bash
brew install maven
```

---

## Ubuntu / Debian

```bash
sudo apt install maven
```

Verify:

```bash
mvn -version
```

---

# 3. Clone or Create the Project

```bash
git clone <repository-url>
cd hello-java-maven
```

or simply create the files shown above.

---

# 4. Compile

```bash
mvn compile
```

Compiled classes will be placed in:

```
target/classes
```

---

# 5. Run

```bash
java -cp target/classes com.example.App
```

Output:

```text
Hello, World!
```

---

# 6. Clean

Remove generated files:

```bash
mvn clean
```

---

# Useful Maven Commands

Compile:

```bash
mvn compile
```

Clean:

```bash
mvn clean
```

Package into a JAR:

```bash
mvn package
```

The JAR will be created in:

```
target/
```

---

# Check Versions

```bash
java -version
javac -version
mvn -version
```


# Structure
```
hello-java-maven/
├── pom.xml
├── README.md
└── src/
    └── main/
        └── java/
            └── com/
                └── example/
                    └── App.java
```