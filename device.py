import time


def show_version(version):
    return (True, {'version': version})


def show_interface_brief(device_name, interface_name):
    interface_status = {
        'ethernet1/1': 'up',
        'ethernet1/2': 'down'
    }
    time.sleep(1)
    if interface_name.lower() in interface_status:
        return (True, {'state': interface_status[interface_name]})
    else:
        return (False, {'error': f'Interface {interface_name} not available.'})


def get_interface_optic_detail(device_name, interface_name):
    optic_detail = {
        'ethernet1/1': {'state':'good', 'rx': '0.98', 'tx': '1.10'},
        'ethernet1/2': {'state':'bad', 'rx': '-30', 'tx': '1.10'}
    }
    if interface_name.lower() in optic_detail:
        return (True, {'state':optic_detail[interface_name]['state'], 'interface_name': optic_detail[interface_name]})
    else:
        return (False, {'error': f'Device {device_name} interface {interface_name} optic detail not available.'})
    

def flap_interface(device_name, interface_name):
    return (True, {'msg': f'Device {device_name} interface {interface_name} came up after shutdown/no shutdown.'})


def check_interface_optic_light_level(device_name, interface_name):
    optic_detail = {
        'ethernet1/1': {'state':'good', 'rx': '0.98', 'tx': '1.10'},
        'ethernet1/2': {'state':'good', 'rx': '0.89', 'tx': '1.10'}
    }
    if interface_name.lower() in optic_detail:
        return (True, {'state':optic_detail[interface_name]['state'], 'interface_name': optic_detail[interface_name]})
    else:
        return (False, {'error': f'Device {device_name} interface {interface_name} optic detail not available.'})


def set_silence_the_device_and_neighbors(device_name):
    return (True, {'message':f'silense set for device {device_name}'})


def collect_snapshot(device_name):
    return (True, {'message':f'snapshot collected from device {device_name}.'})


def get_traffic_drain_config_and_apply(device_name):
    return (True, {'message':f'traffic drain config applied to device {device_name}.'})


def check_if_traffic_goes_away(device_name):
    return (True, {'message':f'Device {device_name} traffic went away.'})


def upgrade_eos_image(device_name, target_eos_version):
    return (True, {'message':f'Device {device_name} has been upgraded to version {target_eos_version}'})


def print_console_info(device_name):
    return (True, {'message':f"Device {device_name}'s console info: ts1-chq2b0140, port01, please login the console to monitor the upgrade process."})


def collect_snapshot_and_compare_previous_snapshot(device_name):
    return (True, {'message':f'Device {device_name} snapshot look good, there is no change between before upgrade and after upgrade.'})


def get_traffic_undrain_config_and_apply(device_name):
    return (True, {'message':f'Device {device_name} has been applied undrain config.'})


def check_if_traffic_comes_back(device_name):
    return (True, {'message':f'Traffic is coming back, Device {device_name} is taking traffic.'})


def clear_alerts(device_name):
    return (True, {'message':f"Cleared the alerts for the device {device_name} and it's neighbors"})


def expire_silence(device_name):
    return (True, {'message':f'expired the silence for device {device_name}'})

