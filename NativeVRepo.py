"""
Copyright © 2025 5kY1iN3. All rights reserved.
NativeVRepo
Version: 1.0
"""
import json
import os
import urllib.request

def download_json(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode('utf-8'))

def snake_to_camel(name):
    return ''.join(word.capitalize() for word in name.split('_'))

def parse_citizenfx_md(content):
    lines = content.split('\n')
    current_section = None
    desc_lines = []
    params = []
    return_value = ''
    notes = []
    examples = {}
    example_lang = None
    example_code = []
    p_type = ''
    p_name = ''
    p_desc = ''

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('# _'):
            continue
        elif stripped == '### Parameters':
            current_section = 'params'
        elif stripped == '### Return Value':
            current_section = 'return'
        elif stripped == '### Notes':
            current_section = 'notes'
        elif stripped == '### Examples':
            current_section = 'examples'
        elif stripped.startswith('#### '):
            if example_lang:
                examples[example_lang] = '\n'.join(example_code).strip()
            example_lang = stripped[5:].strip().lower()
            example_code = []
        elif stripped.startswith('```'):
            if line == '```' and example_lang:  # end of code block
                examples[example_lang] = '\n'.join(example_code).strip()
                example_lang = None
                example_code = []
        elif current_section == 'params':
            if stripped.startswith('* '):
                param_str = stripped[2:].strip()
                parts = param_str.split(' ', 1)
                p_type = parts[0]
                if len(parts) > 1:
                    p_name = parts[1].strip()
                p_desc = ''
            elif line.startswith('  ') and p_name:
                p_desc = stripped
                params.append({'type': p_type, 'name': p_name, 'description': p_desc})
                p_type = ''
                p_name = ''
                p_desc = ''
        elif current_section == 'return':
            if stripped.startswith('* '):
                return_value = stripped[2:].strip()
        elif current_section == 'notes':
            if stripped.startswith('* '):
                notes.append(stripped[2:].strip())
        elif current_section == 'examples' and example_lang:
            example_code.append(line)
        else:
            if current_section is None:
                desc_lines.append(stripped)

    if example_lang:
        examples[example_lang] = '\n'.join(example_code).strip()

    description = ' '.join(desc_lines).strip()

    return {
        'description': description,
        'params': params,
        'return_type': return_value,
        'notes': notes,
        'examples': examples
    }

def generate_md_files(data, base_dir):
    os.makedirs(base_dir, exist_ok=True)
    
    for namespace in data:
        namespace_dir = os.path.join(base_dir, namespace.upper())
        os.makedirs(namespace_dir, exist_ok=True)
        
        for hash_key, native_info in data[namespace].items():
            name = native_info.get('name', 'Unknown')
            camel_name = snake_to_camel(name)
            file_name = f'{camel_name}.md'
            file_path = os.path.join(namespace_dir, file_name)
            
            description = native_info.get('description', 'No description available.')
            params = native_info.get('params', [])
            return_type = native_info.get('return_type', 'void')
            jhash = native_info.get('jhash', '')
            build = native_info.get('build', '')
            examples = native_info.get('examples', [])
            comment = native_info.get('comment', '')
            
            # Fetch and parse CitizenFX MD if available
            cfx_url = f'https://raw.githubusercontent.com/citizenfx/natives/master/{namespace.upper()}/{camel_name}.md'
            cfx_data = None
            try:
                with urllib.request.urlopen(cfx_url) as response:
                    if response.code == 200:
                        cfx_content = response.read().decode('utf-8')
                        cfx_data = parse_citizenfx_md(cfx_content)
            except:
                pass
            
            # Merge missing data from CitizenFX, Alloc8or priority
            if cfx_data:
                if not description or description == 'No description available.':
                    description = cfx_data.get('description', description)
                
                for param in params:
                    if not param.get('description'):
                        matching_params = [p for p in cfx_data.get('params', []) if p['name'] == param.get('name')]
                        if matching_params:
                            param['description'] = matching_params[0]['description']
                
                if cfx_data.get('return_type') and (not return_type or return_type == 'void'):
                    return_type = cfx_data['return_type']
                
                if not comment and cfx_data.get('notes'):
                    comment = '\n'.join(cfx_data['notes'])
                elif cfx_data.get('notes'):
                    comment += '\n' + '\n'.join(cfx_data['notes'])
                
                cfx_examples = cfx_data.get('examples', {})
                for lang, code in cfx_examples.items():
                    if not any(ex['lang'] == lang for ex in examples):
                        examples.append({'lang': lang, 'code': code})
            
            # Write the MD file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f'# _{name}\n\n')
                f.write(f'{description}\n\n')
                
                if params:
                    f.write('### Parameters\n')
                    for param in params:
                        param_name = param.get('name', 'unknown')
                        param_type = param.get('type', 'Any')
                        param_desc = param.get('description', '')
                        f.write(f'* {param_type} {param_name}\n')
                        if param_desc:
                            f.write(f'  {param_desc}\n')
                    f.write('\n')
                
                f.write('### Return Value\n')
                f.write(f'* {return_type}\n\n')
                
                if jhash or build or comment:
                    f.write('### Notes\n')
                    if jhash:
                        f.write(f'* AP Hash: 0x{jhash}\n')
                    if build:
                        f.write(f'* Build: {build}\n')
                    if comment:
                        f.write(f'* {comment}\n')
                    f.write('\n')
                
                if examples:
                    f.write('### Examples\n')
                    for example in examples:
                        lang_type = example.get('lang', 'lua')
                        code = example.get('code', '')
                        f.write(f'#### {lang_type.capitalize()}\n')
                        f.write(f'```{lang_type}\n{code}\n```\n')
                    f.write('\n')

# Download JSON data
legacy_url = 'https://raw.githubusercontent.com/alloc8or/gta5-nativedb-data/master/natives.json'
enhanced_url = 'https://raw.githubusercontent.com/alloc8or/gta5-nativedb-data/master/natives_gen9.json'

legacy_data = download_json(legacy_url)
enhanced_data = download_json(enhanced_url)

# Generate for Legacy
generate_md_files(legacy_data, 'natives/Legacy')

# Generate for Enhanced
generate_md_files(enhanced_data, 'natives/Enhanced')

print('MD files generated successfully in the "natives" directory with individual files per native, merged with additional CitizenFX data where missing.')