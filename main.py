import sys
sys.path.insert(0, 'src/')
import config, json, scraper, keywords


def main():
    journal_list = json.load(open(config.journal_path))
    n = len(journal_list)
    progress = 0
    for journal in journal_list:
        try:
            scraper.get(journal["url"], journal["n"], journal["slug"], journal["path"])
            keywords.exec(journal["slug"])
            progress += 1
            print(str("{:.2f}%".format(progress / n * 100)))
        except Exception as err: 
            print(err)


if __name__ == '__main__':
    main()
