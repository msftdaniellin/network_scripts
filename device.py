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
        return (True, {'state':optic_detail['interface_name']['state'], 'interface_name': optic_detail[interface_name]})
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
        return (True, {'state':optic_detail['interface_name']['state'], 'interface_name': optic_detail[interface_name]})
    else:
        return (False, {'error': f'Device {device_name} interface {interface_name} optic detail not available.'})
