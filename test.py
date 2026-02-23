def build_test_args(args: TestOptions) -> list[str]:
    return (
        (["--dry-run"] if args.dry_run else [])
        + (["--dry-fails", args.dry_fails] if args.dry_fails else [])
        + (["--tests", args.tests] if args.tests else [])
        + [
            "--smoke-runs",
            str(args.smoke_runs),
            "--exec-sequence",
            args.exec_sequence,
            "--run-id",
            args.run_id,
            "--run-name",
            args.run_name,
            "--engine",
            args.test_engine,
            args.results_dir,
            args.config_bundle,
            args.platform,
            args.logger,
            args.exec_mode,
        ]
    )

