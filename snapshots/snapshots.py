import boto3
import click

session = boto3.Session(profile_name='snapshots')
ec2 = session.resource('ec2')


@click.group()
def cli():
    """Snapshots management commands"""

@cli.group('instances')
def instances():
    """Command for instances"""

@cli.group('volumes')
def volumes():
    """Commands for volumes"""

@cli.group('snapshots')
def snapshots():
    """Commands for snapshots"""

@snapshots.command('list')
def list_volumes():
    "List all EC2 volumes"
    instances = []
    for i in ec2.instances.all():
        for v in i.volumes.all():
            for s in v.snapshots.all():
                print (", ".join((
                    s.id,
                    v.id,
                    s.state,
                    s.progress
                )))
    return

@volumes.command('list')
def list_volumes():
    "List all EC2 volumes"
    instances = []
    for i in ec2.instances.all():
        for v in i.volumes.all():
            print (v)
    return


@instances.command('list')
def list_instances():
    "List all EC2 instances"
    instances = []
    for i in ec2.instances.all():
        print (", ".join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name
        )))
    return

@instances.command('snapshot', help="Create snapshots for all volumes")
def create_snapshot():
    for i in ec2.instances.all():
        i.stop()
        i.wait_until_stopped()
        for v in i.volumes.all():
            print('Creating snapshots for {0}'.format(v.id))
            v.create_snapshot(Description="Created by the Python script")
        i.start()
        print('Job\'s done!')
    return


@instances.command('stop')
def stop_instances():
    "Stop all instances"
    instances = ec2.instances.all()
    for i in instances:
        print('Stopping {0}...'.format(i.id))
        i.stop()
    return

@instances.command('start')
def start_instances():
    "Start all instances"
    instances = ec2.instances.all()
    for i in instances:
        print('Starting {0}...'.format(i.id))
        i.start()
    return

if __name__ == '__main__':
    cli()

