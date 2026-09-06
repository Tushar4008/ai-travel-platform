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
    },
    {
        "destination": "Dubai",
        "price": 80000
    }
]

class PackageAnalyzer:
    def __init__(self,packages):
        self.packages = packages

    def get_luxury_packages(self):
        count=0
        luxury_list=[]
        for package in packages:
            if package["price"] >= 100000:
                luxury_list.append(package)
        return luxury_list

    @property
    def luxury_count(self):
        return len(self.get_luxury_packages())


package1=PackageAnalyzer(packages)
print(f"{package1.get_luxury_packages()}")
print(f"Luxury Packages: {package1.luxury_count}")