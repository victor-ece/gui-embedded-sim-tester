#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

class FlashModule {
private:
    std::string executedFilename;

public:
    void setExecFilename(const std::string& filename) {
        executedFilename = filename;
    }

    std::string getExecFilename() const {
        return executedFilename;
    }
};

class TestModule {
public:
    bool runTest(const std::string& filename) {
        int result = system(("python3 " + filename).c_str());
        return result == 0;
    }

    bool compareOutputs(const std::string& codeFile, const std::string& desiredOutput) {
        std::string tempOutput = "temp_output.txt";
        system(("python3 " + codeFile + " > " + tempOutput).c_str());

        // Use the diff command to compare the files
        int result = system(("diff " + tempOutput + " " + desiredOutput).c_str());
        return result == 0;
    }
};

class ReportingModule {
public:
    void reportResult(bool success) {
        std::cout << (success ? "Test Passed" : "Test Failed") << std::endl;
    }
};

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Invalid arguments. Use --success <file> or --compare <file> <desired_output>" << std::endl;
        return 1;
    }

    std::string mode = argv[1];
    FlashModule flash;
    TestModule tester;
    ReportingModule reporter;

    if (mode == "--success" && argc == 3) {
        flash.setExecFilename(argv[2]);
        bool success = tester.runTest(flash.getExecFilename());
        reporter.reportResult(success);
    } else if (mode == "--compare" && argc == 4) {
        flash.setExecFilename(argv[2]);
        bool success = tester.compareOutputs(flash.getExecFilename(), argv[3]);
        reporter.reportResult(success);
    } else {
        std::cerr << "Invalid arguments. Use --success <file> or --compare <file> <desired_output>" << std::endl;
        return 1;
    }

    return 0;
}