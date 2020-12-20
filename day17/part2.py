from common import ConwayCubes


if __name__ == "__main__":
    cc = ConwayCubes(four_dims=True)
    cc.run()
    print(cc.active)
