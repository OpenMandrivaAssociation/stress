Name:         stress
License:      GPL
Group:        System/Kernel and hardware 
Summary:      A tool which imposes a configurable amount of load on your system
Version:      1.0.5
Release:      1
Source0:      https://github.com/resurrecting-open-source-projects/stress/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
URL:          http://weather.ou.edu/~apw/projects/stress/

%description

stress is a tool which imposes a configurable amount of CPU, memory, I/O, or
disk stress on a POSIX-compliant operating system. It is written in
highly-portable ANSI C, and uses the GNU Autotools to compile on a great number
of UNIX-like operating systems.

stress is not a benchmark. It is a tool used by system administrators to
evaluate how well their systems will scale, by kernel programmers to evaluate
perceived performance characteristics, and by systems programmers to expose the
classes of bugs which only or more frequently manifest themselves when the
system is under heavy load. 

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%{_bindir}/stress
%{_infodir}/stress.info.*
%{_mandir}/man1/*
