packages = [
    {
        "destination": "Thailand",
        "price": 55000
    },
    {
        "destination": "Goa",
        "price": 20000
    },
    {
        "destination": "Japan",
        "price": 120000
    }
]

class PackageAnalyzer:

    def __init__(self,packages):
        self.packages=packages

    def get_luxury_packages(self):
        luxury_packages=[]
        for package in self.packages:
            if package['price'] >= 100000:
                luxury_packages.append(package)
        return luxury_packages

package_analyzer = PackageAnalyzer(packages)
print(package_analyzer.get_luxury_packages())
        
