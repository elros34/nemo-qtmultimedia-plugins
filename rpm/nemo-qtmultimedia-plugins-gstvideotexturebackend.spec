# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       nemo-qtmultimedia-plugins-gstvideotexturebackend

# >> macros
# << macros

Summary:    QtMultimedia QML VideoOutput backend for GStreamer NemoVideoTexture interface
Version:    0.0.0
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qtmultimedia-plugins
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-qtmultimedia-plugins-gstvideotexturebackend.yaml
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(nemo-gstreamer-interfaces-1.0)
BuildRequires:  qt5-qtmultimedia-gsttools

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/video/declarativevideobackend/libgstnemovideotexturebackend.so
# >> files
# << files
