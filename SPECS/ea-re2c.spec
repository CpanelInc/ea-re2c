Name: ea-re2c
Version: 3.1
Summary: re2c is a free and open-source lexer generator for C/C++, Go and Rust.
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4556 for more details
%define release_prefix 1
Release: %{release_prefix}%{?dist}.cpanel
License: RE2C License
Group: System Environment/Daemons
Vendor: cPanel, Inc.
URL: https://github.com/skvadrik/re2c
Source: https://github.com/skvadrik/re2c/archive/%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Conflicts: re2c

BuildRequires: python3.11

%description
re2c is a free and open-source lexer generator for C/C++, Go and Rust.

Its main goal is generating fast lexers: at least as fast as their reasonably optimized hand-coded counterparts. Instead of using traditional table-driven approach, re2c encodes the generated finite state automata directly in the form of conditional jumps and comparisons. The resulting programs are faster and often smaller than their table-driven analogues, and they are much easier to debug and understand. re2c applies quite a few optimizations in order to speed up and compress the generated code.

Another distinctive feature is its flexible interface: instead of assuming a fixed program template, re2c lets the programmer write most of the interface code and adapt the generated lexer to any particular environment.

%prep
%setup -q -n re2c-%{version}

%build

echo "XXHEREXX" `pwd`
find . -type f -print

autoreconf -i -W all

export CFLAGS="%{?__global_cflags} -I%{_prefix}/include"
export LDFLAGS='-Wl,-rpath -Wl,%{_libdir} -L%{_libdir}'
export PATH="%{_prefix}/bin:$PATH"

%configure --disable-golang --disable-rust
make -j8

%check

make test

%install
set -x

echo "BUILD ROOT" %{buildroot}

make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%attr(755,root,root) /usr/bin/re2c
/usr/share/man/man1/re2c.1.gz
/usr/share/re2c/stdlib/unicode_categories.re

%changelog
* Fri Oct 04 2024 Julian Brown <julian.brown@cpanel.net> - 3.1-1
- ZC-12239: Initial Release

