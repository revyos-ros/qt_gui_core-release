%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-qt-gui-cpp
Version:        2.0.0
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS qt_gui_cpp package

License:        BSD
URL:            http://ros.org/wiki/qt_gui_cpp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-pluginlib >= 1.9.23
Requires:       ros-rolling-qt-gui >= 0.3.0
Requires:       ros-rolling-rcpputils
Requires:       ros-rolling-tinyxml2-vendor
Requires:       ros-rolling-ros-workspace
BuildRequires:  pkgconfig
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ament-cmake-pytest
BuildRequires:  ros-rolling-pluginlib >= 1.9.23
BuildRequires:  ros-rolling-python-qt-binding >= 0.3.0
BuildRequires:  ros-rolling-rcpputils
BuildRequires:  ros-rolling-tinyxml2-vendor
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
qt_gui_cpp provides the foundation for C++-bindings for qt_gui and creates
bindings for every generator available. At least one specific binding must be
available in order to use C++-plugins.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Apr 07 2021 Dirk Thomas <dthomas@osrfoundation.org> - 2.0.0-4
- Autogenerated by Bloom

* Thu Mar 11 2021 Dirk Thomas <dthomas@osrfoundation.org> - 2.0.0-3
- Autogenerated by Bloom

* Wed Mar 10 2021 Dirk Thomas <dthomas@osrfoundation.org> - 2.0.0-2
- Autogenerated by Bloom

* Mon Mar 08 2021 Dirk Thomas <dthomas@osrfoundation.org> - 2.0.0-1
- Autogenerated by Bloom

