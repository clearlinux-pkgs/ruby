Name     : ruby
Version  : 2.3.0
Release  : 22 
URL      : ftp://ftp.ruby-lang.org/pub/ruby/2.3/ruby-2.3.0.tar.gz
Source0  : ftp://ftp.ruby-lang.org/pub/ruby/2.3/ruby-2.3.0.tar.gz
Summary  : Object Oriented Script Language
Group    : Development/Tools
License  : Ruby MIT TCL
BuildRequires: autoconf
BuildRequires: gdbm-dev
BuildRequires: libffi-dev
BuildRequires: openssl-dev
BuildRequires: yaml-lib
BuildRequires: readline-dev
BuildRequires: zlib-dev
Requires: ruby-bin
Requires: ruby-data
Requires: ruby-doc
Requires: ruby-lib
Requires: rubygems
Requires: rubygem-bigdecimal
Provides: /usr/bin/ruby
# Fake provides
Provides: /usr/local/bin/ruby
Patch1: cve-2015-3900.nopatch

%description
A dynamic, open source programming language with a focus on simplicity 
and productivity. It has an elegant syntax that is natural to read and 
easy to write.

%package bin
Summary: bin components for the ruby package.
Group: Binaries

%description bin
bin components for the ruby package.

%package data
Summary: data components for the ruby package.
Group: Data

%description data
data components for the ruby package.

%package dev
Summary: dev components for the ruby package.
Group: Development
Requires: ruby

%description dev
dev components for the ruby package.

%package doc
Summary: doc components for the ruby package.
Group: Documentation

%description doc
doc components for the ruby package.

%package lib
Summary: lib components for the ruby package.
Group: Binaries

%description lib
bin components for the ruby package.

%package -n rubygem-bigdecimal
Summary: This library provides arbitrary-precision decimal floating-point number class.
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(bigdecimal) = 1.2.8

%description -n rubygem-bigdecimal
This library provides arbitrary-precision decimal floating-point number class.

%package -n rubygem-did_you_mean
Summary: "did you mean?" experience in Ruby: the error message will tell you the right one when you misspelled something. 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(did_you_mean) = 1.0.0

%description -n rubygem-did_you_mean
"did you mean?" experience in Ruby: the error message will tell you the right one when you misspelled something.

%package -n rubygem-io-console
Summary: add console capabilities to IO instances. 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(io-console) = 0.4.5

%description -n rubygem-io-console
add console capabilities to IO instances.

%package -n rubygem-json
Summary: This is a JSON implementation as a Ruby extension in C. 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(json) = 1.8.3

%description -n rubygem-json
This is a JSON implementation as a Ruby extension in C.

%package -n rubygem-minitest
Summary: Minitest provides a complete suite of testing facilities 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(minitest) = 5.8.3

%description -n rubygem-minitest
Minitest provides a complete suite of testing facilities

%package -n rubygem-net-telnet
Summary: Provides telnet client functionality.
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(net-telnet) = 0.1.1

%description -n rubygem-net-telnet
Provides telnet client functionality.

%package -n rubygem-power_assert
Summary: Power Assert for Ruby. 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(power_assert) = 0.2.6 

%description -n rubygem-power_assert
Power Assert for Ruby.

%package -n rubygem-psych
Summary: Psych is a YAML parser and emitter. 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(psych) = 2.0.17

%description -n rubygem-psych
Psych is a YAML parser and emitter.

%package -n rubygem-rake
Summary: Rake is a Make-like program implemented in Ruby.
Group: Development/Tools
Requires: ruby
Requires: rubygems
Provides: rubygem(rake) = 10.4.2

%description -n rubygem-rake
Rake is a Make-like program implemented in Ruby.

%package -n rubygem-rdoc
Summary: RDoc produces HTML and command-line documentation for Ruby projects.
Group: Development/Tools
Requires: ruby
Requires: rubygems
Requires: rubygem-json
Provides: rubygem(rdoc) = 4.2.1

%description -n rubygem-rdoc
RDoc produces HTML and command-line documentation for Ruby projects.

%package -n rubygem-test-unit
Summary: Improved version of Test::Unit 
Group: Development/Tools
Requires: ruby
Requires: rubygems
Requires: rubygem(power_assert)
Provides: rubygem(test-unit) = 3.1.5

%description -n rubygem-test-unit
Improved version of Test::Unit

%prep
%setup -q -n ruby-2.3.0

%build
%configure \
 --prefix=/usr \
 --enable-shared \
 --disable-rpath \
 --with-dbm-type=gdbm_compat \
 --with-out-ext=tcl \
 --with-out-ext=tk

make V=1 %{?_smp_mflags}

%check
make check TESTS="-v $DISABLE_TESTS" ||:

%install
rm -rf %{buildroot}
%make_install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/ruby/2.3.0/English.rb
%{_libdir}/ruby/2.3.0/abbrev.rb
%{_libdir}/ruby/2.3.0/base64.rb
%{_libdir}/ruby/2.3.0/benchmark.rb
%{_libdir}/ruby/2.3.0/cgi.rb
%{_libdir}/ruby/2.3.0/cmath.rb
%{_libdir}/ruby/2.3.0/csv.rb
%{_libdir}/ruby/2.3.0/date.rb
%{_libdir}/ruby/2.3.0/debug.rb
%{_libdir}/ruby/2.3.0/delegate.rb
%{_libdir}/ruby/2.3.0/digest.rb
%{_libdir}/ruby/2.3.0/drb.rb
%{_libdir}/ruby/2.3.0/e2mmap.rb
%{_libdir}/ruby/2.3.0/erb.rb
%{_libdir}/ruby/2.3.0/expect.rb
%{_libdir}/ruby/2.3.0/fiddle.rb
%{_libdir}/ruby/2.3.0/fileutils.rb
%{_libdir}/ruby/2.3.0/find.rb
%{_libdir}/ruby/2.3.0/forwardable.rb
%{_libdir}/ruby/2.3.0/getoptlong.rb
%{_libdir}/ruby/2.3.0/ipaddr.rb
%{_libdir}/ruby/2.3.0/irb.rb
%{_libdir}/ruby/2.3.0/kconv.rb
%{_libdir}/ruby/2.3.0/logger.rb
%{_libdir}/ruby/2.3.0/mathn.rb
%{_libdir}/ruby/2.3.0/matrix.rb
%{_libdir}/ruby/2.3.0/mkmf.rb
%{_libdir}/ruby/2.3.0/monitor.rb
%{_libdir}/ruby/2.3.0/mutex_m.rb
%{_libdir}/ruby/2.3.0/observer.rb
%{_libdir}/ruby/2.3.0/open-uri.rb
%{_libdir}/ruby/2.3.0/open3.rb
%{_libdir}/ruby/2.3.0/openssl.rb
%{_libdir}/ruby/2.3.0/optionparser.rb
%{_libdir}/ruby/2.3.0/optparse.rb
%{_libdir}/ruby/2.3.0/ostruct.rb
%{_libdir}/ruby/2.3.0/pathname.rb
%{_libdir}/ruby/2.3.0/pp.rb
%{_libdir}/ruby/2.3.0/prettyprint.rb
%{_libdir}/ruby/2.3.0/prime.rb
%{_libdir}/ruby/2.3.0/profile.rb
%{_libdir}/ruby/2.3.0/profiler.rb
%{_libdir}/ruby/2.3.0/pstore.rb
%{_libdir}/ruby/2.3.0/resolv-replace.rb
%{_libdir}/ruby/2.3.0/resolv.rb
%{_libdir}/ruby/2.3.0/ripper.rb
%{_libdir}/ruby/2.3.0/rss.rb
%{_libdir}/ruby/2.3.0/scanf.rb
%{_libdir}/ruby/2.3.0/securerandom.rb
%{_libdir}/ruby/2.3.0/set.rb
%{_libdir}/ruby/2.3.0/shell.rb
%{_libdir}/ruby/2.3.0/shellwords.rb
%{_libdir}/ruby/2.3.0/singleton.rb
%{_libdir}/ruby/2.3.0/socket.rb
%{_libdir}/ruby/2.3.0/sync.rb
%{_libdir}/ruby/2.3.0/tempfile.rb
%{_libdir}/ruby/2.3.0/thwait.rb
%{_libdir}/ruby/2.3.0/time.rb
%{_libdir}/ruby/2.3.0/timeout.rb
%{_libdir}/ruby/2.3.0/tmpdir.rb
%{_libdir}/ruby/2.3.0/tracer.rb
%{_libdir}/ruby/2.3.0/tsort.rb
%{_libdir}/ruby/2.3.0/un.rb
%{_libdir}/ruby/2.3.0/unicode_normalize.rb
%{_libdir}/ruby/2.3.0/uri.rb
%{_libdir}/ruby/2.3.0/weakref.rb
%{_libdir}/ruby/2.3.0/webrick.rb
%{_libdir}/ruby/2.3.0/xmlrpc.rb
%{_libdir}/ruby/2.3.0/yaml.rb
%{_libdir}/ruby/2.3.0/cgi/*
%{_libdir}/ruby/2.3.0/digest/sha2.rb
%{_libdir}/ruby/2.3.0/drb/*
%{_libdir}/ruby/2.3.0/fiddle/*
%{_libdir}/ruby/2.3.0/irb/*
%{_libdir}/ruby/2.3.0/matrix/*
%{_libdir}/ruby/2.3.0/net/*
%{_libdir}/ruby/2.3.0/openssl/*
%{_libdir}/ruby/2.3.0/optparse/*
%{_libdir}/ruby/2.3.0/racc/parser.rb
%{_libdir}/ruby/2.3.0/rbconfig/datadir.rb
%{_libdir}/ruby/2.3.0/rexml/*
%{_libdir}/ruby/2.3.0/rinda/*
%{_libdir}/ruby/2.3.0/ripper/*
%{_libdir}/ruby/2.3.0/rss/*
%{_libdir}/ruby/2.3.0/shell/*
%{_libdir}/ruby/2.3.0/syslog/logger.rb
%{_libdir}/ruby/2.3.0/uri/*
%{_libdir}/ruby/2.3.0/unicode_normalize/*
%{_libdir}/ruby/2.3.0/webrick/*
%{_libdir}/ruby/2.3.0/xmlrpc/*
%{_libdir}/ruby/2.3.0/yaml/*
%exclude %{_libdir}/ruby/gems/2.3.0/cache/
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/rbconfig.rb

%files bin
%defattr(-,root,root,-)
%{_bindir}/erb
%{_bindir}/irb
%{_bindir}/ruby

%files data
%defattr(-,root,root,-)
%{_datarootdir}/ri/2.3.0/system/*

%files dev
%defattr(-,root,root,-)
%{_includedir}/ruby-2.3.0/*
%{_libdir}/pkgconfig/ruby-2.3.pc
%{_libdir}/libruby.so
%{_libdir}/libruby.so.2.3
%{_libdir}/libruby.so.2.3.0

%files doc
%defattr(-,root,root,-)
%{_mandir}/man1/erb.1
%{_mandir}/man1/irb.1
%{_mandir}/man1/ruby.1

%files lib
%defattr(-,root,root,-)
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/cgi/escape.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/continuation.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/coverage.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/date_core.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/dbm.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/digest.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/digest/*.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/enc/*
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/etc.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/fcntl.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/fiber.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/fiddle.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/gdbm.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/mathn/*.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/nkf.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/objspace.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/openssl.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/pathname.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/pty.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/racc/cparse.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/readline.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/rbconfig/sizeof.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/ripper.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/sdbm.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/socket.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/stringio.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/strscan.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/syslog.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/thread.so
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/zlib.so

# Files included in rubygems package
%exclude %{_bindir}/gem
%exclude %{_libdir}/ruby/2.3.0/rubygems/*
%exclude %{_libdir}/ruby/2.3.0/rubygems.rb
%exclude %{_libdir}/ruby/2.3.0/ubygems.rb
%exclude %{_datarootdir}/ri/2.3.0/system/Gem/*

%files -n rubygem-bigdecimal
%defattr(-,root,root,-)
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/bigdecimal.so
%{_libdir}/ruby/2.3.0/bigdecimal/*
%{_datarootdir}/ri/2.3.0/system/BigDecimal/*
%{_libdir}/ruby/gems/2.3.0/specifications/default/bigdecimal-1.2.8.gemspec

%files -n rubygem-did_you_mean
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/2.3.0/gems/did_you_mean-1.0.0/
%{_libdir}/ruby/gems/2.3.0/specifications/did_you_mean-1.0.0.gemspec

%files -n rubygem-io-console
%defattr(-,root,root,-)
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/io/*.so
%{_libdir}/ruby/2.3.0/io/console/size.rb
%{_libdir}/ruby/gems/2.3.0/specifications/default/io-console-0.4.5.gemspec

%files -n rubygem-json
%defattr(-,root,root,-)
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/json/ext/*.so
%{_libdir}/ruby/2.3.0/json
%{_libdir}/ruby/2.3.0/json.rb
%{_datarootdir}/ri/2.3.0/system/JSON/*
%{_libdir}/ruby/gems/2.3.0/specifications/default/json-1.8.3.gemspec

%files -n rubygem-minitest
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/2.3.0/specifications/minitest-5.8.3.gemspec
%{_libdir}/ruby/gems/2.3.0/gems/minitest-5.8.3/

%files -n rubygem-net-telnet
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/2.3.0/gems/net-telnet-0.1.1/
%{_libdir}/ruby/gems/2.3.0/specifications/net-telnet-0.1.1.gemspec

%files -n rubygem-power_assert
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/2.3.0/specifications/power_assert-0.2.6.gemspec
%{_libdir}/ruby/gems/2.3.0/gems/power_assert-0.2.6/

%files -n rubygem-psych
%defattr(-,root,root,-)
%{_libdir}/ruby/2.3.0/x86_64-linux-gnu/psych.so
%{_libdir}/ruby/2.3.0/psych/*
%{_libdir}/ruby/2.3.0/psych.rb
%{_libdir}/ruby/2.3.0/psych_jars.rb
%{_datarootdir}/ri/2.3.0/system/Psych/*
%{_libdir}/ruby/gems/2.3.0/specifications/default/psych-2.0.17.gemspec

%files -n rubygem-rake
%defattr(-,root,root,-)
%{_bindir}/rake
%{_libdir}/ruby/gems/2.3.0/gems/rake-10.4.2/
%{_datarootdir}/ri/2.3.0/system/Rake/*
%{_libdir}/ruby/gems/2.3.0/specifications/rake-10.4.2.gemspec

%files -n rubygem-rdoc
%defattr(-,root,root,-)
%{_bindir}/rdoc
%{_bindir}/ri
%{_mandir}/man1/ri.1
%{_libdir}/ruby/2.3.0/rdoc/*
%{_libdir}/ruby/2.3.0/rdoc.rb
%{_datarootdir}/ri/2.3.0/system/RDocTask/*
%{_datarootdir}/ri/2.3.0/system/RDoc/*
%{_libdir}/ruby/gems/2.3.0/specifications/default/rdoc-4.2.1.gemspec
%exclude %{_libdir}/ruby/gems/2.3.0/gems/rdoc-4.2.1/bin/

%files -n rubygem-test-unit
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/2.3.0/specifications/test-unit-3.1.5.gemspec
%{_libdir}/ruby/gems/2.3.0/gems/test-unit-3.1.5/
