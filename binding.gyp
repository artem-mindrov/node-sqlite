{
  'targets': [
    {
      'target_name': 'sqlite3_bindings',
      'sources': [
        './sqlite3_bindings.cc'
      ],
      'dependencies': [
        'deps/sqlite3/binding.gyp:sqlite3'
      ]
    }
  ]
}
