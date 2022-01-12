from setuptools import setup

package_name = 'simple_action_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lsc',
    maintainer_email='chulslee20@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "fibonacci_action_server = simple_action_python.fibonacci_action_server:main",
            "fibonacci_action_client = simple_action_python.fibonacci_action_client:main"
        ],
    },
)
