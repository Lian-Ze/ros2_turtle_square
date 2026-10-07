from setuptools import find_packages, setup

package_name = 'turtle_square'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/draw_square.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lianze',
    maintainer_email='lianze@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'draw_square = turtle_square.draw_square:main',
            'pose_bridge = turtle_square.pose_bridge:main',

        ],
    },
)
