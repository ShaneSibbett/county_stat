from django.core.management.base import BaseCommand
from county_project.settings import BASE_DIR

from myapp.models import Agency, SitePart
import csv
import os


class Command(BaseCommand):
    help = 'Migrate Site and Agency'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Importing data...'))
        base_csv_path = os.getcwd() + '/templates/'
        agency_csv_file = base_csv_path + '/Example School Agency Num 3.csv'
        sitepart_csv_file = base_csv_path + '/Site_Part_example_csv.csv'

        # Saving Agency
        with open(agency_csv_file) as csv_file:
            agency_csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in agency_csv_reader:
                # ['system_name', 'county', 'state', 'active', 'system_type', 'address', 'city', 'zipcode', 'system_no']
                if line_count == 0:
                    system_name_index = row.index('system_name')
                    county_index = row.index('county')
                    state_index = row.index('state')
                    active_index = row.index('active')
                    system_type_index = row.index('system_type')
                    address_index = row.index('address')
                    city_index = row.index('city')
                    zipcode_index = row.index('zipcode')
                    system_no_index = row.index('system_no')
                else:
                    system_name = row[system_name_index]
                    county = row[county_index]
                    state = row[state_index]
                    active = row[active_index]
                    system_type = row[system_type_index]
                    address = row[address_index]
                    city = row[city_index]
                    zipcode = row[zipcode_index]
                    system_no = row[system_no_index]

                    agency = Agency()
                    agency.system_name = system_name
                    agency.county = county
                    agency.state = state
                    agency.active = True if int(active) == 1 else False
                    agency.system_type = system_type
                    agency.address = address
                    agency.city = city
                    agency.zipcode = zipcode
                    agency.system_no = system_no
                    agency.save()

                line_count += 1

        # Saving Site Part
        with open(sitepart_csv_file) as csv_file:
            sitepart_csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in sitepart_csv_reader:
                # ['system_no', 'part_name', 'status', 'sys_site_n']
                if line_count == 0:
                    system_no_index = row.index('system_no')
                    part_name_index = row.index('part_name')
                    status_index = row.index('status')
                    sys_site_n_index = row.index('sys_site_n')
                else:
                    system_no = row[system_no_index]
                    part_name = row[part_name_index]
                    status = row[status_index]
                    sys_site_n = row[sys_site_n_index]

                    # check if agency system no exists
                    agency = Agency.objects.filter(system_no=system_no)
                    if agency.exists():
                        site_part = SitePart()
                        site_part.system_no = agency.first()
                        site_part.part_name = part_name
                        site_part.status = status
                        site_part.sys_site_n = sys_site_n
                        site_part.save()
                    else:
                        message = 'Agency with system_no {} does not exists!'.format(system_no)
                        self.stdout.write(self.style.ERROR(message))
                line_count += 1


        self.stdout.write(self.style.SUCCESS(
            'Data has been successfully imported.'))
