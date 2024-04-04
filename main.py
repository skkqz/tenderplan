from class_tasks import get_links_task, parsing_xml_task


def main():

    get_links = get_links_task.delay()
    list_links = get_links.get()
    parsing_xml_task(list_links)

if __name__ == '__main__':

    print('Start script')
    main()
