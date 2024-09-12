data "external_schema" "sqlalchemy" {
  program = [
    "atlas-provider-sqlalchemy",
    "--path", "./src/example/one",
    "--dialect", "postgresql" // mariadb | postgresql | sqlite | mssql
  ]
}

env "sqlalchemy" {
  src = data.external_schema.sqlalchemy.url
  dev = "docker://mysql/8/dev"
  migration {
    dir = "file://migrations"
  }
  format {
    migrate {
      diff = "{{ sql . \"  \" }}"
    }
  }
}
