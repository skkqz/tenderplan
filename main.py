from tasks import get_data_from_xml, get_links_to_printable_form


def main():
    tasks = get_links_to_printable_form.delay()
    t = tasks.get()
    get_data_from_xml(t)


if __name__ == '__main__':
    print('Start testing workflow...')
    main()
